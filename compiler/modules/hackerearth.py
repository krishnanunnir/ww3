import requests
from coderequests import get_request_id()

RUN_URL = u'https://api.hackerearth.com/v3/code/run/'
COMPILE_URL = u'https://api.hackerearth.com/v3/code/compile/'
CLIENT_SECRET = 'ad4b03ae79f0f3cd3d0ebee7c93baacfcb2471b1'


def run_checker(source,testcase,lang,calltype):

    data = {
        'client_secret': CLIENT_SECRET,
        'async': 1,
        'source': source,
        'lang': lang,
        'time_limit': 5,
        'memory_limit': 262144,
        'input':testcase,
        'id': get_request_id()
    }
    
    if (calltype == 'RUN'):
        r = requests.post(RUN_URL, data=data)
    elif(calltype == 'COMPILE'):
        r = requests.post(COMPILE_URL, data=data)

    return r.json()