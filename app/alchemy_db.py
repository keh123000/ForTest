from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import pymysql

pymysql.install_as_MySQLdb()

# 获取数据库实例
engine = create_engine('mysql+mysqldb://root:123456@192.168.1.178:3306/test')
# 创建会话
Session = sessionmaker(bind=engine)
session = Session()
# 建立映射关系
Base = declarative_base()

md = MetaData(bind=engine)

def add_obj(obj):
    session.add(obj)
    session.commit()
