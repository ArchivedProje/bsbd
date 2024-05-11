from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from client.pyui.profile_window_model import Ui_Form
import base64


class ProfileWindow(QMainWindow, Ui_Form):
    def __init__(self, profile, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_ui(profile)

    def __init_ui(self, profile):
        self.fullNameEdit.setText(profile['full_name'])
        self.fullNameEdit.setReadOnly(True)

        self.phoneNumberEdit.setText(profile['phone_number'])
        self.phoneNumberEdit.setReadOnly(True)

        self.loginEdit.setText(profile['login'])
        self.loginEdit.setReadOnly(True)

        pixmap = QPixmap()
        pixmap.loadFromData(base64.b64decode(profile['photo']))
        pixmap = pixmap.scaled(self.label.size())
        self.label.setPixmap(pixmap)

