#! /usr/bin/env python
# -*- coding: utf-8 -*-

import grpc
import time
from concurrent import futures
from protos import micro_service_pb2, micro_service_pb2_grpc, base_pb2, base_pb2_grpc
import settings
from utils.logger import logger
from handlers import *


# 实现一个派生类,重写rpc中的接口函数.自动生成的grpc文件中比proto中的服务名称多了一个Servicer
class MicroService(micro_service_pb2_grpc.MicroServiceServicer):
    # 重写接口函数.输入和输出都是proto中定义的Data类型
    def DoMicro(self, request, context):
        resp = micro_service_pb2.DoMicroResp()
        do_micro.do_micro(request, resp)
        return resp  # 返回一个类实例


def serve():
    # 定义服务器并设置最大连接数,corcurrent.futures是一个并发库，类似于线程池的概念
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=20))  # 创建一个服务器
    micro_service_pb2_grpc.add_MicroServiceServicer_to_server(MicroService(), grpc_server)  # 在服务器中添加派生的接口服务（自己实现了处理函数）
    grpc_server.add_insecure_port(settings.SERVER_CONF['HOST'] + ':' + settings.SERVER_CONF['PORT'])  # 添加监听端口
    grpc_server.start()  # 启动服务器
    try:
        while True:
            time.sleep(settings._ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpc_server.stop(0) # 关闭服务器

