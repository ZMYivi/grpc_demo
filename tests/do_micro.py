#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 实现了客户端用于发送数据并打印接收到 server 端处理后的数据
import grpc
from protos import micro_service_pb2, micro_service_pb2_grpc

_HOST = '127.0.0.1'
_PORT = '31019'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
    client = micro_service_pb2_grpc.MicroServiceStub(channel=conn)  # 客户端使用Stub类发送请求,参数为频道,为了绑定链接
    req = micro_service_pb2.DoMicroReq()
    req.text = 'micro_req'
    response = client.DoMicro(req)  # 返回的结果就是proto中定义的类
    print("received: ", response)


if __name__ == '__main__':
    run()
