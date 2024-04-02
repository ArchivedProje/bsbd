from PyQt5.QtWidgets import QMainWindow, QLineEdit
from client.pyui.auth_window_model import Ui_Form
from client.pyui.utils import show_error_window, hash_password
import logging


class AuthWindow(QMainWindow, Ui_Form):
    def __init__(self, server_api, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.login_button.clicked.connect(self.__login_btn_pressed)
        self.server_api = server_api
        self.__auth_status = False
        self.__login = ''

    def auth_status(self):
        return self.__auth_status, self.__login

    def __disable_widgets(self):
        self.login_line_edit.setDisabled(True)
        self.password_line_edit.setDisabled(True)
        self.login_button.setDisabled(True)

    def __enable_widgets(self):
        self.login_line_edit.setEnabled(True)
        self.password_line_edit.setEnabled(True)
        self.login_button.setEnabled(True)

    def __login_btn_pressed(self):
        logging.info('login btn pressed')
        if len(self.login_line_edit.text()) == 0:
            logging.warning('login field is empty')
            show_error_window('All fields must be filled in')
            return

        if len(self.password_line_edit.text()) == 0:
            logging.warning('password field is empty')
            show_error_window('All fields must be filled in')
            return

        self.__disable_widgets()
        response = self.server_api.authorize(self.login_line_edit.text(), hash_password(self.password_line_edit.text()))
        self.__enable_widgets()

        if response is None:
            logging.warning('response is none')
            show_error_window('Failed to send request to server. Try again')
            return

        if response.status_code == 200:
            self.__auth_status = True
            self.__login = self.login_line_edit.text()
            self.close()
        elif response.status_code == 403:
            show_error_window('Invalid login or password. Try again')
        else:
            show_error_window('Something went wrong. Try again')
