
a = [126, 44, 33, 123, 43, 67, 90]
b = [34,53,123,42,54]
#把一个元素加到列表的结尾
a.append(35)
a.extend(b)
a.insert(1, '汉字')
a.remove(90)
print(a.pop(1))

a.index(123)
c = a.count(123)
a.sort()
a.reverse()
a.copy()
#a.clear()

print(type(a))
print(a)
print(c)
#print(a)
#------------------------有趣的应用----------------------------------------
list1 = [12, 234, 434, 335]
print([x for x in list1 if x > 234])

print([x*y for x in list1 for y in list1])

print([x+y for x in list1 for y in list1])

print([list1[i]*list1[i] for i in range(len(list1))])
#------------------集合也支持推导式-----------------------
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


#------------------字典-----------------------
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#反向遍历数列
for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):#集合去重复
    print(f)
