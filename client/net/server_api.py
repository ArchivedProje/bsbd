import requests
import logging


class ServerApi:
    def __init__(self, server_url, cert_path):
        self.server_url = server_url
        self.cert_path = cert_path

    @staticmethod
    def __send_get(url, data):
        try:
            return requests.get(url, data, verify=False)
        except Exception as e:
            logging.error(f'failed to send https get request to {url} with data: {data}. error: {e}')
        return None

    @staticmethod
    def __send_post(url, data):
        try:
            return requests.post(url, data, verify=False)
        except Exception as e:
            logging.error(f'failed to send https post request to {url} with data: {data}. error: {e}')
        return None

    def __send_request(self, url, data, req_type):
        possible_requests = {
            'GET': ServerApi.__send_get,
            'POST': ServerApi.__send_post
        }
        if req_type not in possible_requests:
            logging.error(f'got unknown request type: {req_type}')
        logging.info(f'sending request: url: {url}, data: {data}, type: {req_type}')
        response = possible_requests[req_type](self.server_url + f'/{url}', data)
        if response is None:
            logging.info('response is None')
            return response
        logging.info(f'response: text: {response.text}, status_code: {response.status_code}')
        return response

    def authorize(self, login, password):
        data = {'login': login, 'password': password}
        return self.__send_request('authorize', data, 'POST')

    def get_role(self, login):
        data = {'login': login}
        return self.__send_request('role', data, 'GET')

    def get_billings(self, login):
        data = {'login': login}
        return self.__send_request('billings', data, 'GET')

    def get_orders(self, login):
        data = {'login': login}
        return self.__send_request('orders', data, 'GET')

    def get_order(self, order_id):
        data = {'id': order_id}
        return self.__send_request('order', data, 'GET')

    def get_billing(self, billing_id):
        data = {'id': billing_id}
        return self.__send_request('billing', data, 'GET')

    def get_realtor(self, realtor_id):
        data = {'id': realtor_id}
        return self.__send_request('realtor', data, 'GET')

    def get_contract(self, contract_id):
        data = {'id': contract_id}
        return self.__send_request('contract', data, 'GET')
