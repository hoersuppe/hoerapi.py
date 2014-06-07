import requests
from hoerapi.errors import InvalidJsonError, ApiError, NoDataError


API_URL = r'http://hoersuppe.de/api/'


def status():
    try:
        resp = call_api('getLiveByID')
        return resp.status == 0 and resp.msg == 'no ID given'
    except:
        return False


def call_api(action, params={}):
    params = params.copy()
    params['action'] = action

    r = requests.get(API_URL, params=params)

    try:
        rjson = r.json()
    except:
        raise InvalidJsonError(r.text)

    if rjson['status'] != 1:
        raise ApiError(rjson['msg'])

    if 'data' not in rjson:
        raise NoDataError()

    return rjson['data']
