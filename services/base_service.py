# -*- coding: UTF-8 -*-
import json
import grpc
from functools import wraps
from utils.logger import logger
from utils.consul import consul_client
from protos import base_pb2


def rpc_client_wrap(function):
    @wraps(function)
    def decorator(self, *args, **kwargs):
        # rpc请求日志
        logger.info('function: %s, request: {"args": %s, "kwargs": %s}' % (function.__name__, str(args), str(kwargs)))
        ret = function(self, *args, **kwargs)

        # 返回信息处理
        if not ret:
            logger.error("function: %s, rpc return null" % function.__name__)
            return None, ""

        if ret.resp and ret.resp.status == base_pb2.ERROR:
            logger.error("function: %s, rpc error: %s" % (function.__name__, ret.resp.status_message))
            return None, ""

        if ret.resp and ret.resp.status == base_pb2.WARNING:
            logger.warning("function: %s, rpc warning: %s" % (function.__name__, ret.resp.status_message))
            return None, ret.resp.status_message

        logger.info('function: %s, response: %s' % (function.__name__, str(ret)))
        return ret, ""

    return decorator


def init_client(service):
    service_client = None
    rpc_server_addr = ''
    if hasattr(service, 'service_conf'):
        # 若测试ip有配置，调用测试ip微服务，否则走服务发现
        if 'addr' in service.service_conf:
            rpc_server_addr = service.service_conf['addr']
        else:
            _, rpc_server_addr = consul_client.get_service(service.service_conf['name'])

        if not rpc_server_addr:
            logger.error("service recover failed, service name: %s" % service.service_conf['name'])
            return None

        conn = grpc.insecure_channel(rpc_server_addr)
        service_client = service.get_client(conn)

    return service_client


