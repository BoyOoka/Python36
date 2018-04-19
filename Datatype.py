counter = 100          # 整型变量
miles = 1000.0       # 浮点型变量
name = "runoob"     # 字符串

print(counter)
print(miles)
print(name)


a, b, c = 1, 2, "runoob" #为多个对象指定多个变量
print(a,b,c)
#---------------------------------------------------
class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))  # returns True
print(type(A()) == A)      # returns True
print(isinstance(B(), A))    # returns True
print(type(B()) == A)        # returns False

#type()不会认为子类是一种父类类型。isinstance()会认为子类是一种父类类型。
print(3 * 7)  # 乘法
print(2 / 4  )# 除法，得到一个浮点数
print(2 // 4 )# 除法，得到一个整数
print(17 % 3) # 取余
print(2 ** 5) # 乘方

#---------------------------------------------集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)
print(a - b)     # a和b的差集

print(a | b)     # a和b的并集

print(a & b)     # a和b的交集

print(a ^ b)     # a和b中不同时存在的元素
#---------------------------------------------------------字典
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
print(tinydict['site'])

'''
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.quit()
'''

import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='world', charset='utf8')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from city")

# 执行SQL，并返回受影响行数
#effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))

# 执行SQL，并返回受影响行数,执行多次
#effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])


# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()