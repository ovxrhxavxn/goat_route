import customtkinter as CTk
import PIL

from ctkmvc.view import View
from pathlib import WindowsPath

from core.tsp_solver import TSPSolver
from resources.resource import Resource


class MainWindowView(View):

    def __init__(self, controller, model):

        super().__init__(controller, model)

        self._model.add_observer(self)

        self.geometry("460x640")  # Устанавливаем размеры окна
        self.title('G.O.A.T Route')  # Устанавливаем заголовок окна
        self.resizable(False, False)  # Запрещаем изменение размеров окна
        self.iconbitmap(WindowsPath(Resource.ICON).resolve())

        # Устанавливаем тему по умолчанию "Dark"
        CTk.set_appearance_mode("Dark")

        # Загружаем логотип и добавляем его в окно
        self.logo = CTk.CTkImage(

            dark_image=PIL.Image.open(WindowsPath(Resource.LOGO).resolve()),
            size=(160, 160)

            )
        
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0, padx=(20, 20), pady=(20, 0))

        # Создаем фрейм для ввода данных
        self.input_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.input_frame.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self._max_entries = 8

        self._entries_list: list[CTk.CTkEntry] = []  # Список для хранения текстовых полей ввода

        # Добавляем первую панель ввода
        self._add_input_entry()

        # Добавляем текст "KirovChist" между первой панелью ввода и логотипом
        self._kirovchist_label = CTk.CTkLabel(master=self, text="© Киров & Чистяков", fg_color="transparent")
        self._kirovchist_label.grid(row=2, column=0, padx=(20, 20), pady=(10, 0))

        # Создаем фрейм для настроек
        self._settings_frame = CTk.CTkFrame(master=self)
        self._settings_frame.grid(row=3, column=0, padx=(20, 20), pady=(20, 0), sticky="ew")

        # Добавляем радиокнопки в фрейм настроек
        self._radio_var = CTk.StringVar()  # Переменная для связи радиокнопок между собой

        self._radio_buttons = [

            CTk.CTkRadioButton(master=self._settings_frame, text="On Foot",
                                                 variable=self._radio_var, value=TSPSolver.NetworkType.WALK),

            CTk.CTkRadioButton(master=self._settings_frame, text="Car",
                                                 variable=self._radio_var, value=TSPSolver.NetworkType.DRIVE),

            CTk.CTkRadioButton(master=self._settings_frame, text="Public Transport",
                                                 variable=self._radio_var, value=TSPSolver.NetworkType.DRIVE_SERVICE)
        ]

        for i, radio_button in enumerate(self._radio_buttons):
            radio_button.grid(row=0, column=i, padx=(0, 10), sticky="ew")

        # Добавляем кнопку "Генерировать путь" и привязываем ее к методу контроллера generate_path
        self.generate_path_button = CTk.CTkButton(master=self, text="Генерировать путь", 
                                                  
                                                  command=lambda: self._controller.generate_path(
                                                      
                                                    addresses=self._get_addresses_list(),
                                                    network_type = self._get_radio_button_value() 
                                                    
                                                  ))
        

        self.generate_path_button.grid(row=4, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")


    def _add_input_entry(self):

        """Метод для добавления нового текстового поля ввода"""
        
        if len(self._entries_list) < self._max_entries:  # Проверяем, что количество полей меньше максимального
            new_entry_frame = CTk.CTkFrame(master=self.input_frame, fg_color="transparent")
            new_entry_frame.grid(row=len(self._entries_list), column=0, padx=(0, 0), pady=(5, 5), sticky="ew")

            new_entry = CTk.CTkEntry(master=new_entry_frame, width=300)
            new_entry.grid(row=0, column=0, padx=(0, 20))

            self._entries_list.append(new_entry)  # Добавляем новое поле ввода в список

            # Добавляем кнопку "+" для добавления новых полей ввода
            self.btn_add = CTk.CTkButton(master=new_entry_frame, text="+", width=100,
                                         command=self._add_input_entry)
            self.btn_add.grid(row=0, column=1)

            if len(self._entries_list) == self._max_entries:  # Отключаем кнопку, если достигнут максимум
                self.btn_add.configure(state="disabled")


    def _get_addresses_list(self):

        addresses = []

        for i, value in enumerate(self._entries_list):

            addresses.append(value.get())

        return addresses
    

    def _get_radio_button_value(self):

        return self._radio_var.get()


    def model_is_changed(self):
        pass