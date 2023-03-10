import pytest
import requests

from utils.read_sitting import get_sitting
from utils.get_cookies import get_cookies

url = get_sitting['host']['api_ssourl_test1']
headers = {'accept': 'application/json, text/javascript, */*; q=0.01',
           'accept-language': 'zh-CN,zh;q=0.9'}

# token
@pytest.fixture(scope='session')
def get_token():
    url_loginCheck = url + '/loginCheck'
    cookies = get_cookies
    json = {
        "account":"19522301185",
        "passWord": "8cd65c85c7680b4da3b15f898dc74e2a",
        "picCode": "",
        "loginTime": 0
    }
    r = requests.post(url = url_loginCheck,headers = headers,cookies = cookies,json = json)
    result = r.json()
    token = result['data']['token']['token']
    return token
