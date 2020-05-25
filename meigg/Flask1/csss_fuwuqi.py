# -*- coding:utf-8 -*-
# @Time :2020/5/11 9:44
# @Email  :1084928753@qq.com
# @File :csss_fuwuqi.py
import random
import time
from flask import Flask,request,json
xinxin=Flask(__name__)

# @xinxin.route('/')
# def hello():
#     sentence = "520"
#     for char in sentence.split():
#         allChar = []
#         for y in range(12, -12, -1):
#             lst = []
#             lst_con = ''
#             for x in range(-30, 30):
#                 formula = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
#                 if formula <= 0:
#                     lst_con += char[(x) % len(char)]
#                 else:
#                     lst_con += ' '
#             lst.append(lst_con)
#             allChar += lst
#         print('\033[0;32m' + '\n'.join(allChar) + '\033[0m')  # 设置字体颜色和背景
#
#
#
#     return ('\033[0;32m' + '\n'.join(allChar) + '\033[0m')

#创建一个方法来处理请求
#定义一个路由--访问服务的根目录就可以得到结果
@xinxin.route('/')
def hello():
    return '<h1>hello flask</h1>'

#构造一个接受post请求的响应
@xinxin.route('/post',methods=['POST'])
def test_post():
    #处理接口发送过来的两个参数，将两个参数合并成一个字符串返回
    d1=request.form['d1']
    d2=request.form['d2']
    return d1+d2
#处理极简交易接口
@xinxin.route('/trade/purchase',methods=['POST'])
def purchase():
    #拿到客户端返回的数据
    res=json.loads(request.get_data())
    out_trade_no=res['out_trade_no']
    auth_code=res['auth_code']
    data={
        'code': '40004',
        'msg': 'Business Failed',
        'sub_code': 'ACQ.TRADE_HAS_SUCCESS',
        'sub_msg': '交易已被支付',
        'trade_no': '2013112011001004330000121536',
        'out_trade_no': '6823789339978248'
    }
    #把out_trade_no改成客户端发送过来的数据
    data['out_trade_no']=out_trade_no
    data['trade_no']=time.strftime('%Y%m%d%H%M%S')+str(random.random()).replace('0.','')
    #验证授权码
    if auth_code !='28763443825664394':
        return {'coode':'50000','msg':'请求码验证失败'}


    return data

if __name__ == '__main__':
    #运行服务，并确定服务运行的IP和端口
    xinxin.run('127.0.0.1','9090')


