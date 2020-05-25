# -*- coding:utf-8 -*-
# @Time :2020/4/2 11:15
# @Email  :1084928753@qq.com
# @File :test_0001.py
import requests
from HTMLTestRunner_cn import HTMLTestRunner
dict1={'name':'lixia','age':'22'}
for x in dict1.values():
    print(x)
aa=[ 1, 6, 3, 5, 3, 4 ]
dict2={'name':'aming','age':18,'school':'cema'}
for i in dict1.items():
  print(i)

list7=[1,2,3,4,5]
liat8=[ 1, 6, 3, 5, 3, 4 ]
print(liat8.count(6))
a=[23, 65, 19, 90]
a[0]=19
a[2]=23
print(a)
tuple1=(1,2,3,4,5,6)

lis3=list(tuple1)
st2=str(lis3)
print(st2)