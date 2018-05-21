import sys,add  #导入模块
from add import fib2  #导入模块中指定的部分
from add import fib
#from add import *  #导入模块中所有函数
print('命令参数如下：')
for i in sys.argv:
    print(i)
print('路径为：',sys.path,'\n')

print(add.add(3,9))

add.fib(9)
add.fib2(10)
fib(99)
fib2(66)

print(dir(add))