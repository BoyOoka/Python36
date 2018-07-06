#!usr/bin/env python
# encoding:utf-8

def func1(one_list):  
    return list(set(one_list))


def func2(one_list):  
    return {}.fromkeys(one_list).keys()


def func3(one_list):  

    temp_list=[]
    for one in one_list:
        if one not in temp_list:
            temp_list.append(one)
    return temp_list


def func4(one_list):  
    result_list=[]
    temp_list=sorted(one_list)
    i=0
    while i<len(temp_list):
        if temp_list[i] not in result_list:
            result_list.append(temp_list[i])
        else:
            i+=1
    return result_list


if __name__ == '__main__':  
    one_list=[56,7,4,23,56,9,0,56,12,3,56,34,45,5,6,56]
    print(func1(one_list))
    print(func2(one_list))
    print(func3(one_list))
    print(func4(one_list))

