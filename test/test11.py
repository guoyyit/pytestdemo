#Python 标准库概览
from urllib.request import  urlopen
from datetime import date
import zlib
import doctest

#访问 互联网
for line in urlopen('http://jisuye.com/'):
    line = line.decode('utf-8')
    if('http' in line):
        print(line)

#日期和时间
now = date.today()
print(now)
birthday = date(1996,11,9)
print(birthday)
age = now.year - birthday.year
print(age)

#数据压缩
s = b'witch which has which witches wrist watch'
print(len(s))
#压缩
t = zlib.compress(s)
print(len(t))
#解压缩
m = zlib.decompress(t)
print(len(m))
d = zlib.crc32(s)
print(d)


def average(values):
    return sum(values)/len(values)
