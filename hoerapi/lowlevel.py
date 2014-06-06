import requests


API_URL = r'http://hoersuppe.de/api/'


class ApiResponse:
    def __init__(self, status, msg):
        self._status = status
        self._msg = msg

    @property
    def status(self):
        return self._status

    @property
    def msg(self):
        return self._msg


def status():
    resp = call_api('getLiveByID')

    if resp.status == 0 and resp.msg == 'no ID given':
        return True
    else:
        return False


def call_api(action, clazz, params={}):
    params = params.copy()
    params['action'] = action

    r = requests.get(API_URL, params=params)
    rjson = r.json()

    data = rjson.get('data', {})

    return clazz(rjson['status'], rjson['msg'], data)
