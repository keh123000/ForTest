import pymysql
from pymysql.cursors import DictCursor


class MysqlDB(object):
    def __init__(self, host, port: int, user, password, db):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
        self.cursor = self.conn.cursor(DictCursor)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
            print("关闭游标")
        if self.conn:
            self.conn.close()
            print("关闭链接")

    # 执行增删改操作
    def execute(self, sql, data=None):
        result = self.cursor.execute(sql, data)
        self.conn.commit()
        return result

    # 执行查询操作
    def fetch(self, sql, data=None, limit='ALL'):
        self.cursor.execute(sql, data)
        if isinstance(limit, int):
            if limit == 1:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchmany(limit)
        else:
            return self.cursor.fetchall()
