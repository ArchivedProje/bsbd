from PyQt5.QtWidgets import QMainWindow
from client.pyui.main_window_model import Ui_MainWindow
from enum import Enum
import logging


class MainWindowException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"MainWindowException: {self.message}"


class Roles(Enum):
    Client = 1,
    Realtor = 2,
    Performer = 3,
    Admin = 4,
    Unknown = 5


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, server_api, login, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.login = login
        self.server_api = server_api

        if not self.__get_data_from_server():
            raise MainWindowException('failed to get data from server')

    def __get_role(self):
        response = self.server_api.get_role(self.login)
        if response is not None and response.status_code == 200:
            possible_roles = {
                'client': Roles.Client,
                'realtor': Roles.Realtor,
                'performer': Roles.Performer,
                'admin': Roles.Admin
            }
            return possible_roles.get(response.text, Roles.Unknown)
        return None

    def __get_data_from_server(self):
        role = self.__get_role()
        if role is None or role == Roles.Unknown:
            logging.error(f'failed to get role of {self.login}')
            return False
        return True
