from dotenv import load_dotenv
import os
import pyodbc


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class DBHandler:
    def __init__(self):
        self.sql_requests = {
            'get_billings': 'SELECT b.* \
                            FROM agency.dbo.billings b \
                            INNER JOIN agency.dbo.billings_orders bo ON b.id = bo.billing_id \
                            INNER JOIN agency.dbo.orders o ON bo.order_id = o.id \
                            INNER JOIN agency.dbo.clients c ON o.client_id = c.id \
                            WHERE c.login = \'{login}\'',
            'get_orders':   'SELECT o.* \
                            FROM agency.dbo.orders o \
                            INNER JOIN agency.dbo.clients c ON o.client_id = c.id \
                            WHERE c.login = \'{login}\''
        }

    def init(self, path_to_env_file):
        self.__read_env(path_to_env_file)

    def __read_env(self, path_to_env_file):
        load_dotenv(path_to_env_file)
        self.conn = pyodbc.connect(driver=os.getenv('DB_DRIVER'),
                                   server=os.getenv('DB_SERVER'),
                                   database=os.getenv('DB_NAME'),
                                   uid='admin',
                                   pwd='admin',
                                   trusted_connection='yes')

    def __execute(self, request):
        # check for sql injections
        cursor = self.conn.cursor()
        return cursor.execute(request)

    def get_billings(self, login):
        return self.__execute(self.sql_requests['get_billings'].format(login=login))

    def get_orders(self, login):
        return self.__execute(self.sql_requests['get_orders'].format(login=login))

    def close(self):
        self.conn.close()
