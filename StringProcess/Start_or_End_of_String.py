import os
import stat

path = './testdir/'
for fn in os.listdir(path):
    if fn.endswith(('.py','.sh')):
        fs = os.stat(path+fn)
        os.chmod(path+fn,fs.st_mode | stat.S_IXUSR)
