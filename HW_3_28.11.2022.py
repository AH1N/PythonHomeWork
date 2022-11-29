# 3'. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from os import system 
from random import randint
import random
system("cls")


n = int(input(" сколько в саписке элементов?  "))
testList = []


def CreateListFloat(n,testList):
    for i in range(0,n):
         testList.append(randint(0, 2)+ round(random.random(),2))   
    print(testList)

def F(list = testList):
    tempList = []
    for i in testList:
        tempList.append(round(i%1,2))
    testlist = tempList
    testlist.sort(reverse = True)
    print(testlist)
    mi_n = testlist[len(testlist)-1]
    ma_x = testlist[0]
    res = ma_x-mi_n
    print(f"разница {ma_x} и {mi_n} = {round(res,2)}")
    
F(CreateListFloat(n,testList))


