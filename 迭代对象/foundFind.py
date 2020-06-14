#!/bin/python3
# -*- coding: UTF-8 -*-

from collections.abc import Iterable
import requests
from random import sample
import os
import re


class FoundIterable(Iterable):
    def __init__(self, url):
        self.founds = sample(self.fund_find(url),100)

    def __iter__(self):
        for found in self.founds:
            yield self.get_found(found[5:])

    def get_found(self,found):
         try:
            url = "https://api.doctorxiong.club/v1/fund?code=%s" % found
            r = requests.get(url)
            data = r.json()['data'][0]
            return data['name'], data['expectGrowth'], data['lastThreeMonthsGrowth']
         except:
            return "err"

    def fund_find(self,url):
        r = requests.get(url).text
        funds = re.findall('.com/\d{6}',r)
        return set(funds)

class ProcessFound:
    def __init__(self,found):
        self.found = found
        self.buyIn = []
        self.SENDMAIL = "/usr/sbin/sendmail"
        self.sender = "lyj1135154563@163.com"
        self.receviers = "272252973@qq.com"

    def showInfo(self):
        for f in self.found:
            if f == "err":
                continue
            else:
                print("%s 预测今日涨跌幅 %s, 过去三个月涨跌幅 %s" % f)
                if(float(f[1]) < -3 and float(f[2]) >= 30):
                    self.buyIn.append(f[0])
        return len(self.buyIn)

    def mailFound(self):
        subject = "基金信息更新"
        text = "建议买入基金："+" ".join(self.buyIn)
        message = "From:%s\nTo:%s\nSubject:%s\n%s"%(self.sender,self.receviers,subject,text)
        p = os.popen("%s -t -i" % self.SENDMAIL,'w')
        p.write(message)
        status = p.close()
        if status:
            print("Sendmail exit status",status)


if __name__ == "__main__":
    url = u'http://fund.eastmoney.com/allfund.html'
    found = FoundIterable(url)
    pf = ProcessFound(found)
    l = pf.showInfo()
    if l > 0:
        pf.mailFound()
