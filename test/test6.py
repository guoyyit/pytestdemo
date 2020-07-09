# python 数据结构
#Python中列表是可变的，这是它区别于字符串和元组的最重要的特点，一句话概括即：列表可以修改，而字符串和元组不能
from collections import deque
#只有当前目录有init文件时才能导入
from test.test7 import say_hello

say_hello()
print(dir(say_hello))

list = []
for i in range(20):
    list.append(i)

list.reverse()
print(list)
list.sort()
print(list)

#将列表当做堆栈使用
stack = [4,5,6]
print(stack.pop())
print(stack)

#将列表当作队列使用  popleft 移去并且返回一个元素，deque最左侧的那一个
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)
print(queue.popleft())
print(queue)

#列表推导式
vec = [2,4,6]
print([3*x for x in vec])
print([[x, x**2] for x in vec])

#嵌套列表解析
 #matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
 #print([[row[i] for row in matrix] for i in range(4)])

 #del 语句
adel = [-1, 1, 66.25, 333, 333, 1234.5]
del adel[0]
print(adel)
#: 时直接清空list
del adel[:]
print(adel)

#元组和序列
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

#集合 集合是一个无序不重复元素的集 类似java set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

str1=set('abracadabra')
str2=set('alacazam')
print('str1:',str1)
print('str2:',str2)
#str1中唯一的字母
print("str1中唯一的字母:",str1-str2)
#在str1和str2中都有的字母
print("在str1和str2中都有的字母:",str1&str2)
#在str1中的字母，但不在str2中
print("在str1中的字母，但不在str2中:",str1-str2)
#在str1或str2中的字母
print("在str1或str2中的字母:",str1|str2)
#在str1或str2中的字母，但不同时在str1和str2中
print("在str1或str2中的字母，但不同时在str1和str2中:",str1^str2)
#集合推导式
strs = {x for x in 'abracadabra' if x not in 'abc'}
print(strs)

#字典 类似于java.Map
tel = {'jack': 4098, 'sape': 4139}
#dict 可将数组转换为map
mm = [('sape', 4139), ('guido', 4127), ('jack', 4098)]
print(dict(mm))
#遍历map
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for key,value in knights.items():
    print(key,value)
#在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for index, value in enumerate(['tic', 'tac', 'toe']):
    print(index,value)
#同时遍历两个或更多的序列，可以使用 zip() 组合：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(q,a)
#要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
for i in reversed(range(1, 10, 2)):
    print(i)
#要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(basket):
    print(f)
print('--------------------------')
for f in sorted(set(basket)):
    print(f)