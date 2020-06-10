from functools import reduce

def MaxList(l:list)->int:
    return reduce(lambda x,y: max(x,y), l)

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7]
    i = MaxList(l)
    print(i)
