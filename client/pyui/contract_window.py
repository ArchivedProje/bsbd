from PyQt5.QtWidgets import QMainWindow
from client.pyui.contract_window_model import Ui_Form


class ContractWindow(QMainWindow, Ui_Form):
    def __init__(self, contract, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_ui(contract)

    def __init_ui(self, contract):
        self.contractNumberLbl.setText(f'Договор №{contract["contract_number"]}')

        self.regNumberEdit.setText(str(contract["reg_number"]))
        self.regNumberEdit.setReadOnly(True)

        self.detailsEdit.setText(contract["details"])
        self.detailsEdit.setReadOnly(True)
