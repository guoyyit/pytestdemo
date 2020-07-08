# python 迭代器与生成器
import sys
list = []
for s in range(100):
    list.append(s)

print(len(list))
print(list)

# it = iter(list)
# for x in it:
#     print(x)
#     pass

# boolean = True;
# while(boolean):
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

def fibonacci(n):
    a,b,counter = 0,1,0
    while(True):
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10)

while(True):
    try:
        print(next(f),end="")
    except StopIteration:
        sys.exit()