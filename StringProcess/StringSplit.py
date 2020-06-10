import re
from functools import reduce

class StringProcess(object):
    def __init__(self):
        self.string = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
        self.seps = ';|,\t'

    def stringSplit(self):
        #str.split
        s = self.string.split(';')
        s = ''.join(s)
        s = s.split('|')
        s = ''.join(s)
        s = s.split(',')
        s = ''.join(s)
        s = s.split('\t')
        s = ''.join(s)
        print(s)

    def stringSplit1(self):
        res = [self.string]
        for sep in self.seps:
            t = []
            list(map(lambda ss: t.extend(ss.split(sep)), res))
            res = t
        print(''.join(res))

    def stringSplit2(self):
        # 字符串分割
        return reduce(lambda l,sep: sum(map(lambda ss:ss.split(sep),l)), self.seps,[self.string])

my_split = lambda s,seps: reduce(lambda l,sep: sum(map(lambda ss:ss.split(sep),l)), seps,[s])

class Person(object):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class LambdaTest(object):
    def __init__(self):
        self.person = []

    def add_person(self,obj:object):
        self.person.append(obj)

    def sort_by_age(self):
        res = sorted(self.person,key=lambda x: x.age)
        return res
    def sorted_by_height(self):
        return sorted(self.person,key=lambda x:x.height)

if __name__ == "__main__":
  #  S = StringProcess()
  #  S.stringSplit()
  #  S.stringSplit1()
    string = 'ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
    res = re.split('[\t,|;]+',string)
    print("name,age,height,weight:")
    L = LambdaTest()
    while True:
        name = input()
        if(name == "exit"):
            break
        age =int(input())
        height = int(input())
        weight = int(input())
        p = Person(name,age,height,weight)
        L.add_person(p)

    res = L.sort_by_age()
    for i in res:
        print(i.name)















