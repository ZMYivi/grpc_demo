# -*- coding: UTF-8 -*-
from peewee import *
from enum import unique, Enum
from playhouse.pool import PooledMySQLDatabase
from playhouse.shortcuts import ReconnectMixin


class RetryMySQLDatabase(ReconnectMixin, PooledMySQLDatabase):
    _instance = None

    @staticmethod
    def get_db_instance():
        if not RetryMySQLDatabase._instance:
            RetryMySQLDatabase._instance = RetryMySQLDatabase(
                'dashuju',
                max_connections=20,
                stale_timeout=300,
                host='60.205.215.111',
                user='root',
                password='initial123',
                port=30002
            )
        return RetryMySQLDatabase._instance


# 如何使用？
# 在model文件中
database = RetryMySQLDatabase.get_db_instance()
#
# # 连接数据库
# database = MySQLDatabase('dashuju', user='root', host='60.205.215.111', port=30002, password='initial123')
#

@unique
class AreaStatus(Enum):
    normal = 1
    delete = 2


# 定义Person
class Area(Model):
    id = IntegerField(primary_key=True)
    name = CharField(default='')
    parent_id = IntegerField(default=0)
    status = IntegerField(default=0)
    create_time = DateTimeField()
    modify_time = DateTimeField()

    class Meta:
        database = database


def run():
    # 数据库访问测试
    with database.connection_context():
        #
        全部输出data = Area.select().dicts()
    print(list(data))

    pass


if __name__ == "__main__":
    run()



