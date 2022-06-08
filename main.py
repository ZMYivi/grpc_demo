#! /usr/bin/env python
# -*- coding: utf-8 -*-

from server import serve
from utils.logger import logger

if __name__ == '__main__':
    logger.logger.info('service start')
    serve()
