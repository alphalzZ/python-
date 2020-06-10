from random import randint, sample
from functools import reduce
class Com_key:
  def __init__(self):
    self.name = 'adnfjasf'
    self.d1 = {k: randint(1,3) for k in sample(self.name, randint(3,6))}
    self.d2 = {k: randint(1,3) for k in sample(self.name, randint(3,6))}
    self.d3 = {k: randint(1,3) for k in sample(self.name, randint(3,6))}
    self.dl = [self.d1,self.d2,self.d3]

  def find_comkey1(self):
      comm = [key for key in self.d1.keys() if key in self.d2.keys() and key in self.d3.keys()]
      print(comm)

  def find_comkey2(self):
      comm = [k for k in self.dl[0] if all(map(lambda x: k in x,self.dl[1:]))]
      print(comm)

  def find_commkey3(self):
      comm = reduce(lambda a,b: a&b, map(dict.keys, self.dl))
      print(comm)

  def map_test(self):
      comm = list(map(lambda x:x+"15", self.name))
      print(comm)

  def reduce_test(self):
      #阶乘
      res = reduce(lambda a, b: a * b, range(1,10), 1)
      print(res)

def main():
  score = Com_key()
  score.find_comkey1()
  score.find_comkey2()
  score.find_commkey3()
  score.map_test()
  score.reduce_test()

if __name__ == '__main__':
  main()


