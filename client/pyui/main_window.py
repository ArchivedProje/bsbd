from PyQt5.QtWidgets import QMainWindow
from client.pyui.main_window_model import Ui_MainWindow
from client.pyui.order_window import OrderWindow
from enum import Enum
import logging
import json


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

        self.ordersBtn.clicked.connect(self.__show_orders)
        self.listWidget.itemClicked.connect(self.__show_specific_order)
        self.__show_orders()

    def __show_specific_order(self, item):
        self.listWidget.setEnabled(False)
        try:
            order_id = int(item.text().split()[1]) - 1
        except ValueError:
            return
        order_window = OrderWindow(self.orders[order_id], self.server_api, self)
        order_window.show()
        self.listWidget.setEnabled(True)

    def __show_orders(self):
        self.listWidget.clear()
        for idx, order in enumerate(self.orders):
            self.listWidget.addItem(f'Заказ: {idx + 1} от {order["start_date"]}. Статус: {order["status"]}')

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

    def __handle_orders_response(self, msg):
        try:
            self.orders = json.loads(msg)
        except ValueError as e:
            logging.warning(f'invalid json: {e}')
            return False
        return True

    def __get_client_data(self):
        response = self.server_api.get_orders(self.login)
        if response is None or response.status_code != 200:
            return False
        if not self.__handle_orders_response(response.text):
            return False
        return True

    def __get_realtor_data(self):
        pass

    def __get_performer_data(self):
        pass

    def __get_admin_data(self):
        pass

    def __get_data_from_server(self):
        role = self.__get_role()
        if role is None or role == Roles.Unknown:
            logging.error(f'failed to get role of {self.login}')
            return False
        possible_roles = {
            Roles.Client: self.__get_client_data,
            Roles.Realtor: self.__get_realtor_data,
            Roles.Admin: self.__get_admin_data,
            Roles.Performer: self.__get_performer_data
        }

        return possible_roles[role]()
