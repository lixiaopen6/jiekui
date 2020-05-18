# -*- coding:utf-8 -*-
# @Time :2020/3/11 13:52
# @Email  :1084928753@qq.com
# @File :login.py


import logging,yaml,os,pymysql
logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)  # 输出所有大于DEBUG级别的log
# 设置日 志输出格式
fmt = logging.Formatter('[%(filename)-6s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')
stream_hdl = logging.StreamHandler()
stream_hdl.setFormatter(fmt)
stream_hdl.setLevel(logging.DEBUG)
logger.addHandler(stream_hdl)