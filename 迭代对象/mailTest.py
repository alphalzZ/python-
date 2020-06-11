#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
SENDMAIL = "/usr/sbin/sendmail"
sender = "lyj1135154563@163.com"
receviers = "272252973@qq.com"
subject = "Test"
text = "这是一个测试邮件"
message = "From:%s\nTo:%s\nSubject:%s\n%s"%(sender,receviers,subject,text)
print(message)
p = os.popen("%s -t -i" % SENDMAIL,'w')
p.write(message)
status = p.close()
if status:
    print("Sendmail exit status",status)

