

if __name__ == '__main__':#等于main时在模块自身运行
   print('程序自身在运行')
else:
   print('我来自另一模块')


def add(a,b):
    return a+b


def fib(n):    # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
