# 3'. Задайте последовательность чисел. 
# Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
from random import randint
from os import system 
system("cls")


n = int(input(" сколько в саписке элементов?  "))
testList = []

def CreateSpisok(n,testList):
    for i in range(0,n):
        testList.append(randint(0, 10))
        testList.sort()
    print(testList)

def Nepovtorimie(list = testList):
    tempList = []
    testList.sort()
    for i in range(0,len(testList)-1):
        if testList[i]==testList[i+1]:
            continue
        else:
            tempList.append(testList[i])
    tempList.append(testList[len(testList)-1])       
    print(tempList)

Nepovtorimie(CreateSpisok(n,testList))



