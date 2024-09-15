from dotenv import load_dotenv

from mvc.controllers import MainWindowController
from mvc.models import MainWindowModel
from mvc.views import MainWindowView


def main():

    load_dotenv()

    MainWindowController(
        
        MainWindowView,
        MainWindowModel()
        
        )
    
if __name__ == '__main__':
    main()