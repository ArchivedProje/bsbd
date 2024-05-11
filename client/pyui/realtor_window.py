from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from client.pyui.realtor_window_model import Ui_Form
from client.pyui.response_window import ResponseWindow


class RealtorWindow(QMainWindow, Ui_Form):
    def __init__(self, realtor, login, server_api, parent=None):
        self.login = login
        self.server_api = server_api
        super().__init__(parent)
        self.setupUi(self)
        self.__init_ui(realtor)
        self.addResponseBtn.clicked.connect(self.__add_response)

    def __init_ui(self, realtor):
        self.realtor_id = realtor['id']

        self.fullNameEdit.setText(realtor["full_name"])
        self.fullNameEdit.setReadOnly(True)

        self.ratingEdit.setText('{:1.2f}'.format(realtor["rating"]))
        self.ratingEdit.setReadOnly(True)

        self.experienceEdit.setText(str(realtor["experience"]))
        self.experienceEdit.setReadOnly(True)

        self.phoneNumberEdit.setText(realtor["phone_number"])
        self.phoneNumberEdit.setReadOnly(True)

        pixmap = QPixmap()
        pixmap.loadFromData(realtor['photo'])
        pixmap = pixmap.scaled(self.label.size())
        self.label.setPixmap(pixmap)

        for response in realtor['responses']:
            self.responsesList.addItem(response)

    def __add_response(self):
        response_window = ResponseWindow(self.login, self.realtor_id, self.server_api, self)
        response_window.show()
