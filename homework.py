

def mySort(list):
    newList = []
    for i in range(len(list)):
        j = i
       # print(list[i])
        while j < len(list):
            j += 1
            if(j == len(list)):
                break
            if(list[i]>list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
        newList.append(list[i])
        # print(newList)
    return newList


print(mySort([1238, 342, 24, 123, 412, 215, -1, 42, 124, 0, 1, 999, 789]))

