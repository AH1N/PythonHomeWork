# Реализуйте алгоритм перемешивания списка.


from os import system 
from random import shuffle
from random import randint
system("cls")


# n = int(input(" сколько в саписке элементов?  "))
# testList = []

# def CreateSpisok(n,testList):
#     for i in range(0,n):
#         testList.append(i)
#     print(testList)
# CreateSpisok(n,testList)

testList = [x for x in range(0,int(input(" сколько в саписке элементов?  ")))]
new_list = testList

# def ShakeElem(l_ist):
#     index_1 = randint(0,len(testList)-1)
#     index_2 = randint(0,len(testList)-1)
#     temp1 = testList[index_1]
#     temp2 = testList[index_2]
#     testList[index_1] = temp2
#     testList[index_2] = temp1
def ShakeElem(new_list):
    print(f"{new_list}---ДО ПОМЕШАТЕЛЬСТВА")
    shuffle(new_list)
    print(f"{new_list}---ПОСЛЕ ПОМЕШАТЕЛЬСТВА")
    return new_list

ShakeElem(new_list)

# skolko_pomeshat = int(input("сколько помешать?:  "))
# for i in range(skolko_pomeshat):
#     ShakeElem(testList) 
# print(testList)


