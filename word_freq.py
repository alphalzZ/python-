import re
from collections import Counter
if __name__ == '__main__':
  txt = open('/etc/yum.conf').read()
  word = re.split('\W+',txt)
  count = Counter(word)
  print(count.most_common(10))

