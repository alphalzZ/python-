from random import randint

class orderdict():
    def __init__(self):
        self.rank_dict = {
            name:randint(30,80) for name in 'abcdefghijklmn'
        }
    def dict_sort(self):
        order_dict = sorted(self.rank_dict, key = self.rank_dict.values(),reverse=True)
        result = {
            k:(i,v) for i,(k,v) in enumerate(order_dict.items(), 1)
        }
        print(result)


if __name__ == "__main__":
    print("main 函数执行。")
    od = orderdict()
    od.dict_sort()

