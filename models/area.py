# -*- coding: UTF-8 -*-
from peewee import *
from enum import unique, Enum
from utils.mysql import COMMON_DB
from settings import COMMON_MYSQL
import time

class Area(Model):
    id = IntegerField(primary_key=True)
    name = CharField(default='')
    parent_id = IntegerField(default=0)
    status = IntegerField(default=0)
    create_time = DateTimeField()
    modify_time = DateTimeField()

    class Meta:
        db_table = 'area'
        database = COMMON_DB


# struct类型转response
def model_to_resp_data(model_data, resp_data):
    resp_data.id = model_data.id
    resp_data.name = model_data.name
    resp_data.parent_id = model_data.parent_id
    resp_data.status = model_data.status
    resp_data.create_time = int(model_data.create_time.timestamp())
    resp_data.modify_time = int(model_data.modify_time.timestamp())
    pass


# dict类型转response
def dict_to_resp_data(model_data, resp_data):
    resp_data.id = model_data['id']
    resp_data.name = model_data['name']
    resp_data.parent_id = model_data['parent_id']
    resp_data.status = model_data['status']
    resp_data.create_time = int(model_data['create_time'].timestamp())
    resp_data.modify_time = int(model_data['modify_time'].timestamp())
    pass

