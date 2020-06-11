#!/bin/python3
# encoding=utf8
from collections.abc import Iterable
import requests


class FoundIterable(Iterable):
    def __init__(self, founds):
        self.founds=founds

    def __iter__(self):
        for found in self.founds:
            yield self.get_found(found)

    def get_found(self,found):
         url = "https://api.doctorxiong.club/v1/fund?code=%s" % found
         r = requests.get(url)
         data = r.json()['data'][0]
         return data['name'], data['expectGrowth'], data['lastThreeMonthsGrowth']

class ProcessFound:
    def __init__(self,found):
        self.found = found
        self.buyIn = []
    def showInfo(self):
        for f in self.found:
            print("%s 预测今日涨跌幅 %s%,过去三个月涨跌幅 %s%" % f)
            if(f[1] < -1 and f[2] >=10):
                self.buyIn.append(f[0])

    def mailFound(self):
        pass
if __name__ == "__main__":
    found = FoundIterable(['160222','160219','008282',\
        '160213','001630','001549','001595','519732','161725'])
    pf = ProcessFound(found)
    pf.showInfo()
    pf.mailFound()
