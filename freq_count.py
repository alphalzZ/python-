from random import randint
import heapq
from collections import Counter

if __name__ == '__main__':

  l = [randint(0,10) for _ in range(50)]
  count = Counter(l)
  print("Counter:", count.most_common(3))
  d = {i:0 for i in set(l)}
  for i in l:
    d[i] += 1
  order_d = sorted(d.items(),key=lambda x:x[1],reverse=True)
  print("oder_d:",order_d)
  lagest3 = heapq.nlargest(3, ((v,k) for k,v in d.items()))
  print("heapq:",lagest3)

