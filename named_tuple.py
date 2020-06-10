#-*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
##  问题描述：tuple非常好用，但是在索引的时候缺乏意义，
##  导致程序可读性差
# 解决方案1.为每一个位置定义意义,如下：
from enum import IntEnum
from collections import namedtuple
NAME, AGE, SEX = range(0,3)
class Tea(IntEnum):
  AGE = 0
  NAME = 1
class Stu(IntEnum):
  NAME = 0
  AGE = 1
  SEX =2
def main():  
  student = ('jim',16,'F')
  print(student[NAME])
  print(student[AGE])
  print(student[Stu.NAME])
  print(student[Stu.AGE])
  teacher = (24, '李老师')
  print(teacher[Tea.AGE])
  print(teacher[Tea.NAME])
  # 3.
  stu = namedtuple('Student', ['name','age', 'gender'])
  s1 = stu('jim',16,'男')
  print(s1.gender)
  print(s1.name)
  print(s1.age)
if __name__ == '__main__':
  main()
  print('F5  test!')


