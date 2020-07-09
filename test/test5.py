# python 函数
#不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
#可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

def hello(a):
    a=a+100
    return a

b = hello(20)
print('b是：',b)

#不定长参数  加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def printinfo(arg1,*vartuple):
    print(arg1)
    print(vartuple)

printinfo("甲","乙","丙")

#加了两个星号 ** 的参数会以字典的形式导入
def printinfo2(arg2,**var):
    print(arg2)
    print(var)

printinfo2(1,a=2,b=3)

def f(a,b,*,c):
    return a+b+c

print(f(1,2,c=3))