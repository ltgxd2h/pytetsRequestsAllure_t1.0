from utils.mysql_utils import db

class getMysql():
    def queryCustomerCostRecord(self,n):
        r = db.select_db_one(
                         'SELECT COUNT(id) as num FROM `smarthr-finance`.`product_bill_detail` WHERE cust_id = {}'.format(n))
        return r

getmysql = getMysql()

if __name__ == '__main__':
    print(getmysql.queryCustomerCostRecord(989527231799119914)['num'])