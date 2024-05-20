import sys

from PySide6.QtWidgets import QApplication

from os import getenv
from dotenv import load_dotenv

from utilities.mapping.map import Map
from utilities.mapping.geolocation import Coordinate
from views.gui.main_window import MainWindow


def main():
    load_dotenv()

    

if __name__ == '__main__':
    main()