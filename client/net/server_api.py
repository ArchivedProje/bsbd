import requests
import logging


class ServerApi:
    def __init__(self, server_url, cert_path):
        self.server_url = server_url
        self.cert_path = cert_path

    def authorize(self, login, password):
        data = {'login': login, 'password': password}
        url = self.server_url + '/authorize'
        logging.info(f'sending authorize request to {url}')
        try:
            response = requests.post(self.server_url + '/authorize', data, verify=False)
            logging.info(f'received response: msg: {response.text}, status_code: {response.status_code}')
            return response.status_code == 200
        except Exception as e:
            logging.error(f'failed to send https request. error: {e}')
        return False
