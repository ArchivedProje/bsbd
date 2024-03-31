from PyQt5.QtWidgets import QMainWindow, QLineEdit
from client.pyui.auth_window_model import Ui_Form
from client.pyui.utils import show_error_window
from client.net.server_api import ServerApi
import logging


class AuthWindow(QMainWindow, Ui_Form):
    def __init__(self, callback_on_success, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.login_button.clicked.connect(self.__login_btn_pressed)
        self.callable = callback_on_success

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

        if ServerApi.authorize(self.login_line_edit.text(), self.password_line_edit.text()):
            logging.info('authorization is successful')
            self.callable()
        else:
            logging.warning('authorization failed')

