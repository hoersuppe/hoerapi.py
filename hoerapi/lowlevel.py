import requests
from hoerapi.errors import InvalidJsonError, ApiError, NoDataError


API_URL = r'http://hoersuppe.de/api/'


def status():
    try:
        rjson = requests.get(API_URL, params={ 'action': 'getLiveByID' }).json()
        return rjson['status'] == 0 and rjson['msg'] == 'no ID given'
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
