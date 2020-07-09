#Python 输入和输出
import pickle

s = 'Hello, Runoob'
print(str(s))
print(repr(s))

print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

# str = input("输入:");
# print("输出",str)

f = open("D:\\pythonworkspace\\studypython\\test\\file\\a.txt", "w")
num = f.write("哈哈哈哈，嘻嘻嘻，啦啦啦啦")
print(num)
print('tell',f.tell())
f.close()

f2 = open("D:\\pythonworkspace\\studypython\\test\\file\\a.txt", "r")
#print(f2.read())
#str = f2.readline()
#str = f2.readlines()
#print(str)
for line in f2:
    print(line)
f2.close()

f3 = open("D:\\pythonworkspace\\studypython\\test\\file\\a.txt", "rb+")
print('f3',f3.read())
print(f3.seek(5))
print(f3.read(1))
f3.close()

data1 = {'a': [1, 2.0, 3, 4+6j],'b': ('string', u'Unicode string'),'c': None}
print(data1)
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
print(selfref_list)
output = open("D:\\pythonworkspace\\studypython\\test\\file\\b.txt", 'wb')
data1 = str(data1).encode("GBK")
selfref_list = str(selfref_list).encode("GBK")
pickle.dump(data1,output)
pickle.dump(selfref_list,output)
output.close()