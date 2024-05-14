import json

from requests import Session, HTTPError, RequestException
from enum import StrEnum

from . api_client_interfaces import I2GISAPIClient, ITSPSolver
from .. geolocation import Coordinate
    

class TSPAPIClient(I2GISAPIClient, ITSPSolver):

    '''
    Класс-клиент для работы с 2GIS TSP API 
    '''

    __BASE_ENDPOINT = 'https://routing.api.2gis.com/logistics/vrp/1.1.0/'

    class Task:

        '''
        Класс, представляющий созданную задачу
        '''

        class Status(StrEnum):

            '''
            Enum статусов готовности задачи
            '''

            RUN = 'Run'
            DONE = 'Done'
            PARTIAL = 'Partial'
            FAIL = 'Fail'

        class Solution:
            pass

        def __init__(self, task_id: int):

            self._task_id = task_id
            self._status = TSPAPIClient.Task.Status.RUN
            self._url_solution = None
            self._url_excluded = None

        @property
        def task_id(self) -> int:
            return self._task_id
        
        @property
        def status(self) -> Status:
            return self._status

        @status.setter
        def status(self, value: Status):
            self._status = value

        @property
        def url_solution(self):
            return self._url_solution
        
        @property
        def url_excluded(self):
            return self._url_excluded
            
    @property
    def base_endpoint(self):
        return self.__BASE_ENDPOINT
    
    def __get_task(self, json_task: str) -> Task:

        response = json.loads(json_task)
        
        task_id = response['task_id']

        return TSPAPIClient.Task(task_id=task_id)


    def __make_body_for_request(self, waypoints: list[Coordinate]) -> dict:

        body = {

            'agents': [

                {
                    'agent_id': 0,
                    'start_waypoint_id': 0
                }
            ],

            'waypoints': []
        }

        for i in range(len(waypoints)):

            body['waypoints'].append({

                'waypoint_id': i,

                'point': {

                    'lat': waypoints[i].latitude,
                    'lon': waypoints[i].longitude
                }
            })

        return body

    def solve_tsp(self, waypoints: list[Coordinate]) -> Task:

        body = self.__make_body_for_request(waypoints=waypoints)

        headers = {

            'Content-Type': 'application/json'
        }

        try:

            with Session() as s:

                response = s.post (

                    url=f'{self.__BASE_ENDPOINT}create?key={self._apikey}', data=json.dumps(body), headers=headers
                )

        except HTTPError as e:
            print(f'{e.response.status_code}, {e.response.text}')

        except RequestException as e:
            print(e.response.text)

        else:
            
            try:
                return self.__get_task(response.text)
            
            except Exception as e:
                print(e)
        
    def __assign_status_to_task(self, json_response: str, task: Task) -> Task.Status:

        response = json.loads(json_response)

        status: str = response['status']

        for s in task.Status:

            if status == s:

                task.status = s

                return s
            
    def __assign_solution_to_task(self, json_response: str, task: Task):

        response = json.loads(json_response)

        if task.status == task.Status.DONE:
            task._url_solution = response['urls']['url_vrp_solution']

        else:
             task._url_solution = response['urls']['url_vrp_solution']
             task._url_excluded = response['urls']['url_excluded']

    def check_task_status(self, task: Task) -> Task.Status:

        try:

            with Session() as s:

                response = s.get(

                    url=f'{self.__BASE_ENDPOINT}status?task_id={task.task_id}&key={self._apikey}'
                )

        except HTTPError as e:
            print(e.response.text)

        except RequestException as e:
            print(e.response.text)

        else:
            
            try:
                status = self.__assign_status_to_task(response.text, task=task)

                if status in (task.Status.DONE, task.Status.PARTIAL):
                    self.__assign_solution_to_task(json_response=response.text, task=task)

                    return status
            
                else:
                    return status
                
            except Exception as e:
                print('Что-то пошло не так... Повторите попытку позже.')