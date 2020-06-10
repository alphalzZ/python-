# 字典排序
from random import randint

if __name__ == '__main__':
  d = {k:randint(50,100) for k in 'abcdefg'}
  l = [(v,k) for k,v in d.items()]
  l = sorted(l,reverse=True)
  #2.
  d = sorted(d.items(),key = lambda x:x[1], reverse=True)
  # print(d)
  order = {k:(i,v) for i,(k,v) in enumerate(d,1)}
  print(order)

