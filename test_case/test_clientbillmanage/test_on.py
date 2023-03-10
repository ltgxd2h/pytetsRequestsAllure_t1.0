import allure
import pytest
import requests

from utils.get_mysql import getmysql
from utils.read_sitting import get_sitting
from utils.read_yaml import get_yaml

url = get_sitting['host']['api_url_test1']
headers = {'accept': 'application/json, text/javascript, */*; q=0.01',
           'accept-language': 'zh-CN,zh;q=0.9',}

# def test_one(get_token):
#     t = get_token
#     print(t)


@allure.epic("项目模块")
@allure.feature("客户账单管理")
class TestClientBillManage():

    @allure.story("客户费用查询")
    @allure.title("测试手机号归属地title")
    @allure.testcase("http://www.baidu.com", name="接口地址testcase")
    @allure.issue("http://www.baidu.com", name="缺陷地址issue")
    @allure.link("http://www.baidu.com", name="链接地址link")
    @allure.description("当前手机号是13456755448，归属地是杭州的description")
    @allure.step("先进性归属地的操作step")
    @allure.severity("critical")

    @pytest.mark.parametrize('custid,status',get_yaml['clientStatus'])
    def test_queryCustomerCostRecord(self,get_token,custid,status):
        url1 = url + '/finance/productBillDetail/queryCustomerCostRecord'
        # t = get_token
        headers['token'] = get_token
        headers['aid'] = '4034188388001'
        json = {'custId': custid,
                'status': status,
                'pageNum': 1,
                'pageSize': 30}
        r = requests.post(url = url1,headers = headers,json = json)
        allure.attach(f"请求方法：{r.request.method}\n请求路径：{r.request.url}\n请求参数：{r.request.body}\n请求头：{r.request.headers}\n"
                      f"响应信息：{r.text}","请求及响应详情：",allure.attachment_type.TEXT)

        result = r.json()
        assert result['errorCode'] == 'S000000'
        assert result['errorMsg'] == '操作成功'
        if status == 'null':
            assert result['data']['total'] == getmysql.queryCustomerCostRecord(989527231799119914)['num']

        # print(result)

if __name__ == '__main__':
    pytest.main(['-vs','test_on.py'])

