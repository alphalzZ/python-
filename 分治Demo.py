

def FalseCoin(coin,low,high):
    if(low+1==high):
        if coin[low]>coin[high]:
            return high
        return low
    length = len(coin)
    if(length%2==0):
        weight1 = sum(coin[low:int((low+high)/2)])
        weight2 = sum(coin[int((low+high)/2):high])
        if weight1>weight2:
            return FalseCoin(coin,int((low+high)/2),high)
        elif weight1<weight2:
            return FalseCoin(coin,low,int((low+high)/2))
if __name__ == "__main__":
    coin = [2,2,2,2,2,1,2,2,2,2]
    l = len(coin)
    flag = l%2==0
    if flag:
        print(FalseCoin(coin,0,l))
    else:
        print(FalseCoin(coin[:-1],0,l-1))



