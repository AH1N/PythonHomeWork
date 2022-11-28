# Реализуйте алгоритм перемешивания списка.


from os import system 
from random import randint
system("cls")


n = int(input(" сколько в саписке элементов?  "))
testList = []


def CreateSpisok(n,testList):
    for i in range(0,n):
        testList.append(i)
    print(testList)


CreateSpisok(n,testList)


def ShakeElem(l_ist):
    index_1 = randint(0,len(testList)-1)
    index_2 = randint(0,len(testList)-1)
    temp1 = testList[index_1]
    temp2 = testList[index_2]
    testList[index_1] = temp2
    testList[index_2] = temp1
    

skolko_pomeshat = int(input("сколько помешать?:  "))

for i in range(skolko_pomeshat):
    ShakeElem(testList)


print(testList)