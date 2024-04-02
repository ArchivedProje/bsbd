from flask import Flask, make_response

app = Flask(__name__)


class HttpsServer:
    def __init__(self, cert_path, key_path):
        self.cert_path = cert_path
        self.key_path = key_path

    def run(self):
        app.run(host='0.0.0.0', port=443, ssl_context=(self.cert_path, self.key_path))


@app.route('/authorize', methods=['POST'])
def authorize():
    return make_response('authorized', 200)


@app.route('/role', methods=['GET'])
def get_role():
    return make_response('client', 200)


@app.route('/billings', methods=['GET'])
def get_billings():
    return make_response('', 200)


@app.route('/orders', methods=['GET'])
def get_orders():
    return make_response('', 200)
