
n = 100

sum = 0
counter = 1
ttt=40
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n,sum))
print("1 到 %d 之和为:%drwe%d"  %(n,sum,ttt))
'''
var = 1
while var == 1 :  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print ("你输入的数字是: ", num)

print ("Good bye!")
'''
count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:
    print (count, " 大于或等于 5")


sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

test = ['a','b','c','d','g']
print(len(test))
for i in range(5,9) :#range指定区间的值
    print(i)
for i in range(0, 10, 3) :#range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
    print(i)
for i in range(-10, -100, -30) :
    print(i)
a = ('Google', 'Baidu', 'Runoob', 'Taobao', 'QQ')
for i in range(len(a)):
        print(i, a[i])
print(list(range(5)))#range()函数来创建一个列表

#break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
for letter in 'Runoob':     # 第一个实例
    if letter == 'b':
        break
    print ('当前字母为 :', letter)

var = 10                    # 第二个实例
while var > 0:
    print ('当期变量值为 :', var)
    var = var -1
    if var == 5:
        break

print ("Good bye!")

#!/usr/bin/python3

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
#continue
for letter in 'Runoob':     # 第一个实例
    if letter == 'o':        # 字母为 o 时跳过输出
       # break
        continue
    print ('当前字母 :', letter)

var = 10                    # 第二个实例
while var > 0:
    var = var -1
    if var == 5:             # 变量为 5 时跳过输出
        continue
    print ('当前变量值 :', var)
print ("Good bye!")

#else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

#迭代器
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
for x in it:
    print (x, end=" ")

import sys         # 引入 sys 模块

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象

while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()


import sys

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()