from PyQt5.QtWidgets import QMainWindow
from client.pyui.realtor_window_model import Ui_Form


class RealtorWindow(QMainWindow, Ui_Form):
    def __init__(self, realtor, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_ui(realtor)

    def __init_ui(self, realtor):
        self.fullNameEdit.setText(realtor["full_name"])
        self.fullNameEdit.setReadOnly(True)

        self.ratingEdit.setText('{:1.2f}'.format(realtor["rating"]))
        self.ratingEdit.setReadOnly(True)

        self.experienceEdit.setText(str(realtor["experience"]))
        self.experienceEdit.setReadOnly(True)

        self.phoneNumberEdit.setText(realtor["phone_number"])
        self.phoneNumberEdit.setReadOnly(True)
