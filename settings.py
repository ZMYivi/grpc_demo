#! /usr/bin/env python
# -*- coding: utf-8 -*-

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

SERVER_CONF = dict(
    HOST='0.0.0.0',  # 注意只能是0.0.0.0，不然部署docker外网无法访问
    PORT='31019',
)

LOG_PATH = 'log/all.log'

COMMON_MYSQL = dict(
    database_name='dashuju',
    consul_name='mysql',
    user='root',
    password='initial123',
    # cli='mysql -h 10.105.240.128 -u root -P 30306 -proot',
)

CONSUL_SERVER = dict(
    HOST="60.205.215.111",  # consul服务器的ip
    PORT="30004",  # consul服务器对外的端口
)
