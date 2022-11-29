# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 

from os import system 
from random import randint
system("cls")


n = int(input(" сколько в саписке элементов?  "))
testList = []


def CreateSpisok(n,testList):
    for i in range(0,n):
        testList.append(randint(0, 10))
    print(testList)


def ProizvedKrajElem(list = testList):
    tempList = []
    for i in range(0,len(testList)//2):
        tempList.append(testList[i]*testList[(len(testList)-1)-i])
    if len(testList)%2 > 0:
        tempList.append(testList[(len(testList)//2)]**2)
    print(tempList)


ProizvedKrajElem(CreateSpisok(n,testList))