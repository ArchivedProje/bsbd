from PyQt5.QtWidgets import QMainWindow
from client.pyui.billing_window_model import Ui_Form


class BillingWindow(QMainWindow, Ui_Form):
    def __init__(self, billing, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_ui(billing)
        self.closeBtn.clicked.connect(self.close)

    def __init_ui(self, billing):
        self.priceEdit.setText(str(billing["price"]))
        self.priceEdit.setReadOnly(True)

        self.statusEdit.setText(billing["status"])
        self.statusEdit.setReadOnly(True)

        self.paymentDateEdit.setText(billing["payment_date"])
        self.paymentDateEdit.setReadOnly(True)
