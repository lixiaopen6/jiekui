# -*- coding:utf-8 -*-
# @Time :2020/6/2 11:03
# @Email  :1084928753@qq.com
# @File :cs.py



#定义一个List，任意输入10个数字保存到List。
lis = [1,33,44,22,84,46,2,5,8,99,0]
# for a in range(1,11):
#     number=int(input("请输入一个数字："));
#     lis.append(number);
#冒泡排序(从左往右推)

# for cs in range(len(lis)):
#     for index in range(len(lis)-1):
#         if lis[index]>lis[index+1]:
#             lis[index], lis[index + 1] = lis[index + 1], lis[index];
# print(lis)

for i in range(len(lis)):
    for j in range(len(lis)-1):
        if lis[j]>lis[j+1]:
            lis[j],lis[j+1]=lis[j+1],lis[j]
print(lis)