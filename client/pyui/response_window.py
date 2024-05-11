from PyQt5.QtWidgets import QMainWindow
from client.pyui.response_window_model import Ui_Form
from client.pyui.utils import show_success_window, show_error_window


class ResponseWindow(QMainWindow, Ui_Form):
    def __init__(self, login, realtor_id, server_api, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.login = login
        self.realtor_id = realtor_id
        self.server_api = server_api
        self.sendResponseBtn.clicked.connect(self.__send_response)
        self.cancelBtn.clicked.connect(self.close)

    def __send_response(self):
        msg = self.textEdit.toPlainText()
        response = self.server_api.add_response(self.login, msg, self.realtor_id)
        if response.status_code == 200:
            show_success_window('Ваш отзыв успешно добавлен')
        else:
            show_error_window('Не удалось добавить отзыв. Попробуйте позже')
        self.close()
