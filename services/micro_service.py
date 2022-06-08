# -*- coding: UTF-8 -*-

from protos import micro_service_pb2, micro_service_pb2_grpc, base_pb2, base_pb2_grpc
from services.base_service import rpc_client_wrap, init_client
from utils.consul import consul_client
import grpc


@rpc_client_wrap
def do_micro(text, *args, **kwargs):
    _, rpc_server_addr = consul_client.get_service("micro_service")
    with grpc.insecure_channel(rpc_server_addr) as channel:
        stub = micro_service_pb2_grpc.MicroServiceStub(channel)
        resp = stub.DoMicro(micro_service_pb2.DoMicroReq(
            text=text
        ), timeout=1)
    return resp


class MicroService:
    def __init__(self):
        self.service_conf = dict(
            name='micro_service',  # 服务名
            # addr='127.0.0.1:31019',  # 测试使用ip
        )
        self.service_client = init_client(self)  # 初始化客户端

    def get_client(self, conn):
        return micro_service_pb2_grpc.MicroServiceStub(channel=conn)  # 定义服务端连接类型

    # rpc调用函数封装
    @rpc_client_wrap
    def do_micro(self, text, *args, **kwargs):
        req = micro_service_pb2.DoMicroReq()
        req.text = text

        return self.service_client.DoMicro(req)


micro_service_client = MicroService()
