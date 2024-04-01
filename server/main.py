import os
import logging
import datetime
from server.net.https_server import HttpsServer


def init_logger():
    today_date = datetime.datetime.now().strftime('%d-%m-%Y')
    file_handler = logging.FileHandler(f'server_{today_date}.log')

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, console_handler])


def main():
    init_logger()

    server = HttpsServer(os.path.abspath('../secrets/cert.pem'), os.path.abspath('../secrets/key.pem'))
    server.run()


if __name__ == '__main__':
    main()
