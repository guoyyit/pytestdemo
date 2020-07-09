#Python 错误和异常
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError as err:
        print(err)
        print("您输入的不是数字，请再次尝试输入！")

# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self,value):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as a:
    print(a.value)