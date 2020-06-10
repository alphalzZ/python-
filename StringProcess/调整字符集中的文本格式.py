# 字符串匹配
import re
log = open('./testdir/yum.log').read()
print(log)
# 匹配，分组，命名
log_new = re.sub(r'(?P<m>\d{2}):(?P<y>\d{2}):(?P<j>\d{2})',r'\g<m>/\g<y>/\g<j>',log)
print(log_new)

data = open('./testdir/log.txt').read()
print(data)
data_new = re.findall(r'\d+.\d+|\d+',data)
print(data_new)


