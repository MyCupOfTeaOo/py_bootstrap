"""
    日志配置
"""
import logging
import os
import re

# 读取日志转储地址
import logstash
from colorama import init
from qg_common_sdk.returnInfo import get_request_id
from termcolor import colored

init()

_suffix = re.compile('\n$')

LOG_FORMAT = "%(asctime)s.%(msecs)03d-%(requestId)s-%(threadName)s-%(levelname)s(%(name)s:%(" \
             "filename)s:%(funcName)s[line:%(" \
             "lineno)d]): %(message)s  "
DATE_FORMAT = "%Y-%m-%d,%H:%M:%S"


class QueueHandler(logging.Handler):

    def emit(self, record):
        if not record.getMessage() or record.getMessage() == '\n' or record.getMessage() == '\r\n':
            return
        record.requestId = get_request_id()
        if record.levelname == 'ERROR':
            print(colored(_suffix.sub('', self.format(record), 1), 'red'))
        elif record.levelname == 'INFO':
            print(colored(_suffix.sub('', self.format(record), 1), 'green'))
        elif record.levelname == 'WARNING':
            print(colored(_suffix.sub('', self.format(record), 1), 'yellow'))
        else:
            print(colored(_suffix.sub('', self.format(record), 1), 'cyan'))


def init_log():
    from .config import config
    cust_handler = QueueHandler()
    cust_handler.setFormatter(logging.Formatter(
        datefmt=DATE_FORMAT, fmt=LOG_FORMAT))
    logging.basicConfig(level=config['log_level'], handlers=(
        cust_handler, logstash.TCPLogstashHandler(host=config['logstash']['host'], port=config['logstash']['port'],
                                                  message_type=config['app_name'])))
    version = config.get('version')
    if logging.root.level == logging.WARNING:
        print('初始化日志前 不允许使用 logging 打印')
        os._exit(1)
    logging.info(f'版本号: {version}')
