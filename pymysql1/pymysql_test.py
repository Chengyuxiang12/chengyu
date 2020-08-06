import pymysql

import json


def query(sql):
    db = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="db_morning")
    cur = db.cursor()
    cur.execute(sql)
    res = cur.fetchall()  # 保存结果
    db.close()
    return res


# sql = "select * from tb_goods"
# res = query(sql)
#
# print(len(res))
def commit(sql):
    db = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="db_morning")
    cur = db.cursor()
    cur.execute(sql)
    db.commit()  # 提交修改（事务）
    db.close()
