from dotenv import load_dotenv

from models.main_window_model import MainWindowModel
from controllers.main_window_controller import MainWindowController
from views.ui.gui import MainWindowGUI

def main():

    load_dotenv()

    MainWindowController(
        
        MainWindowGUI(),
        MainWindowModel()
        
        )
    
if __name__ == '__main__':
    main()