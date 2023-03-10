import pymysql

from utils.read_sitting import get_sitting

# host = get_sitting['mysql']['user']
#
# print(host)
#
# db = pymysql.connect(
#     host = 'sh-cdb-p6ronbka.sql.tencentcdb.com',
#     port = 63947,
#     user = 'global_rw',
#     password = 'wBQrEv2If8I8',
#     database = 'smarthr-finance',
#     charset= "utf8"
# )
#
# cursor = db.cursor()
#
# sql = 'select * from hro_saas_cost limit 10'
# cursor.execute(sql)
#
# result = cursor.fetchall()
#
# print(result)
#
#
# # DB_CONF = {
# #     "host": 'sh-cdb-p6ronbka.sql.tencentcdb.com',
# #     "port": 63947,
# #     "user": 'global_rw',
# #     "password": 'wBQrEv2If8I8',
# #     "db": 'smarthr-finance'
# # }
# #
# #
class MysqlDb:
    def __init__(self):
        # mysql连接
        # self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.conn = pymysql.connect(
            host='sh-cdb-p6ronbka.sql.tencentcdb.com',
            port=63947,
            user='global_rw',
            password='wBQrEv2If8I8',
            database='smarthr-finance',
            charset="utf8"
        )
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    # 查询一条
    def select_db_one(self, sql):
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchone()
        return result

    # 查询多条
    def select_db_all(self, sql):
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchall()
        return result

    def execute_db(self, sql):
        try:
            print('执行sql')
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print('执行sql有误')


db = MysqlDb()
if __name__ == '__main__':
    db = MysqlDb()
    result = db.select_db_all(
        "select * from hro_saas_cost limit 10")
    print(result[0]['id'])
