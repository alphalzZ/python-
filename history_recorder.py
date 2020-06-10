from random import randint
from collections import deque
import pickle
import os
class GuessNum():
    def __init__(self):
        self.num = randint(0,100)
        self.que = deque([],5)
    def guess(self,num):
        if num>self.num:
            print("bigger")
            return 0
        if num<self.num:
            print("smaller")
            return 0
        if num==self.num:
            print("biggno")
            return 1
    def history(self):
        print(list(self.que))
if __name__ == "__main__":
    flag = 0
    g = GuessNum()
    if os.path.exists("que.pkl"):
        with open("que.pkl",'rb') as f:
            g.que = pickle.load(f)
    while(flag!=1):
        try:
            num = input()
            if num == "h":
                g.history()
                continue
            elif num=="e":
                with open("que.pkl",'wb') as f:
                    pickle.dump(g.que,f)
                break
            else:
                g.que.append(int(num))
            flag = g.guess(int(num))
        except Exception as e:
            print(e)


