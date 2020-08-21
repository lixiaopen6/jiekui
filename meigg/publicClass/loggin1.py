# -*- coding:utf-8 -*-
# @Time :2020/6/1 15:39
# @Email  :1084928753@qq.com
# @File :loggin1.py

import  logging,time
# format="%(asctime)s %(name)s %(levelname)s %(message)s 文件%(filename)s  函数%(funcName)s  行数%(lineno)d"
# aa="%Y_%m_%d_%H:%M:%S"
# logging.basicConfig(format=format,datefmt=aa,level=logging.ERROR,
#                     filename=' {}_log1.txt'.format(time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())))
# logging.error("错误数据2")


def logger():
    format="%(asctime)s %(name)s %(levelname)s %(message)s 文件%(filename)s  函数%(funcName)s  行数%(lineno)d"
    bb="%Y_%m_%d_%H:%M:%S"
    # 第二种方式是使用Logging日志系统的四大组件
    logger=logging.getLogger('logger')
    #日志输出的最低级别（忽略当前最低级别以下级别的日志信息）
    logger.setLevel(logging.ERROR)
    # 创建控制台处理
    sh=logging.StreamHandler()
    # 创建文件处理器
    fh=logging.FileHandler(filename="{}_log2.txt".format(time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())),encoding="utf-8")
    # 把控制台处理器添加到日志器中
    logger.addHandler(sh)
    # 指定格式器显示的格式
    formatter=logging.Formatter(fmt=format,datefmt=bb)
    # 控制台处理器指定格式
    sh.setFormatter(formatter)
    # 添加文件处理器到日志器
    logger.addHandler(fh)
    fh.setFormatter(formatter)
    return logger










