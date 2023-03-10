import pytest
import requests

from utils.read_sitting import get_sitting

url = get_sitting['host']['api_ssourl_test1']
headers = {'accept': 'application/json, text/javascript, */*; q=0.01',
           'accept-language': 'zh-CN,zh;q=0.9'}

def test_get_cookies():
    url_loginPage = url + '/loginPage'

    r = requests.get(url = url_loginPage, headers = headers)

    cookies = r.cookies.get_dict()
    return cookies

get_cookies = test_get_cookies()