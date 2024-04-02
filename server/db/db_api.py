from dotenv import load_dotenv
import os
import pyodbc


class DBHandler:
    def __init__(self, path_to_env_file):
        self.__read_env(path_to_env_file)

    def __read_env(self, path_to_env_file):
        load_dotenv(path_to_env_file)
        self.conn = pyodbc.connect(driver=os.getenv('DB_DRIVER'),
                                   server=os.getenv('DB_SERVER'),
                                   database=os.getenv('DB_NAME'),
                                   uid='admin',
                                   pwd='admin',
                                   trusted_connection='no')

    def get_billings(self, login):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT id FROM clients WHERE login == {login}')
        client_id = cursor.fetchone()
        if client_id is None:
            return None
        return cursor.execute(f'SELECT * FROM billings WHERE client_id == {client_id}')

    def close(self):
        self.conn.close()
