#同级目录下引用需要init文件来初始化
from test.testpackage.a import *
__all__ = ["test1","test2"]

if __name__ == '__main__':
    print("程序自身在运行")
else:
    print('我来自另一模块')

