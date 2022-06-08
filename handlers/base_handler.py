#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
from functools import wraps
from utils.logger import logger
from protos import base_pb2
import traceback


def rpc_server_wrap(function):
    @wraps(function)
    def decorator(request, response):
        try:
            # 打印请求日志
            logger.logger.info('function: %s, request: %s' % (function.__name__, str(request)))
            function(request, response)
        except Exception as e:
            # 打印报错日志，并返回报错提示
            logger.logger.error('%s\n request: %s' % (traceback.format_exc(), str(request)))
            response.resp.status_message = str(e)
            response.resp.status = base_pb2.ERROR
            return
        logger.logger.info('response: %s' % (str(response)))
        return
    return decorator