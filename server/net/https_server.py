from flask import Flask, make_response, request
from server.db.db_api import DBHandler
import json

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
    if 'login' not in request.args:
        return make_response('login field not found', 404)
    res = DBHandler().get_billings(request.args['login'])
    if res is None:
        return make_response('internal server error', 500)
    out = list()
    for row in res:
        out.append({
            'id': row[0],
            'status': row[1],
            'price': row[2],
            'payment_date': row[3].strftime("%Y-%m-%d %H:%M:%S")
        })
    return make_response(json.dumps(out), 200)


@app.route('/orders', methods=['GET'])
def get_orders():
    if 'login' not in request.args:
        return make_response('login field not found', 404)
    res = DBHandler().get_orders(request.args['login'])
    if res is None:
        return make_response('internal server error', 500)
    out = list()
    for row in res:
        order = {
            'id': row[0],
            'client_id': row[1],
            'realtor_id': row[2],
            'status': row[3],
            'start_date': row[4].strftime("%Y-%m-%d %H:%M:%S")
        }
        if row[5] is not None:
            order['end_date'] = row[5].strftime("%Y-%m-%d %H:%M:%S")
        out.append(order)
    return make_response(json.dumps(out), 200)
