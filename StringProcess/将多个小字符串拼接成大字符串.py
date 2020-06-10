# coding:utf-8
from functools import reduce

s = ['li','zhng','fas']
S = ''.join(_ for _ in s)  # 最好的方法
S = reduce(str.__add__, s)  # 有时间和空间上的浪费

print(S)

