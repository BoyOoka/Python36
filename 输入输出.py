s = 'Hello world\n'
x=9 ;y=8
print(str(s))
print(repr(s)) #可以转译字符串的特殊字符
# repr() 的参数可以是 Python 的任何对象
print(repr((x, y, ('Google', 'Runoob'))))
#str.format() 的基本使用如下:
print('{}网址： "{}!"哈哈这个{}！'.format('菜鸟教程', 'www.runoob.com','有意思'))
#在括号中的数字用于指向传入对象在 format() 中的位置
print('{2}网址： "{0}!"哈哈这个{1}！'.format('菜鸟教程', 'www.runoob.com','有意思'))
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print(table.keys(),table.values())
#---------------------------------------------------------------------------------------
#a = input('请输入一个参数：')
#open(filename, mode)open() 将会返回一个 file 对象
f = open("C:/Users/gaya/Desktop/12.txt","a")
#f.write("this is a test\n,and i like it!")
#b = f.read()
#print(b,1)
#f.seek(4)
#print(f.tell())
f.close()
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('C', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()