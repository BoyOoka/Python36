# -*- coding: utf-8 -*-
print("Hello World!")
print("中文")
#中文注释

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    print ("False")    # 缩进不一致，会导致运行错误

total = 'item_one' + \
        'item_two' + \
        'item_three'

total2 = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
total3 = {'item1','item2','item3'}

print(total,total2,total3)
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

str='Runoob'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
print(paragraph[0:-1],end="")#不换行

print('------------------------------')

print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


#input("\n按下 enter 键后退出。")
import sys
print('================Python import mode==========================');
print ('命令行参数为:')

for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)