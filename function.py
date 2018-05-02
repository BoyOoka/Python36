def add(a,b):
    return print(a+b)


add(3,4)

def ChangeInt( a ):
    a = 10
    return a
 #   print(a)

b=2
print(ChangeInt(b))
print( b ) # 结果是 2

def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print ("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)

def printme( str ):
    "打印任何传入的字符串"
    print (str)
    return

#调用printme函数
printme(str="菜鸟教程")


#可写函数说明
def printinfo( name, age ):
    "打印任何传入的字符串"
    print ("名字: ", name)
    print ("年龄: ", age)
    return

#调用printinfo函数
printinfo( age=50, name="runoob" )

#可写函数说明
def printinfo2( name, age = 35 ):
    "打印任何传入的字符串"
    print ("名字: ", name)
    print ("年龄: ", age)
    return

#调用printinfo函数
printinfo2( age=50, name="runoob" )
print ("------------------------")
printinfo2( name="runoob" )

# 可写函数说明
def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print ("输出: ")
    print (arg1)
    for var in vartuple:
        print (var)
    return

# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 'ttt',456,'法施工' )