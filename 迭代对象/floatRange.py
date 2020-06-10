

class FloatRange:
    def __init__(self,a,b,step):
        self.a = a
        self.b = b
        self.step = step
    def __iter__(self):
        t = self.a
        while round(t,2) <= self.b:
            yield round(t,2)
            t += self.step
    def __reversed__(self):
        t = self.b
        while round(t,2) >= self.a:
            yield round(t,2)
            t -= self.step
if __name__ == "__main__":
    fr = FloatRange(2,4,0.2)
    for i in fr:
        print(i)
    print('*'*10)
    for i in reversed(fr):
        print(i)
