# 1'. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


from os import system 
from random import randint
system("cls")


n = int(input(" сколько в саписке элементов?  "))
testList = []


def CreateSpisok(n,testList):
    for i in range(0,n):
        testList.append(randint(0, 10))
    print(testList)



def Summ4etElements(list = testList):
    res = 0
    for i in range(len(testList)):
        if i == 0 or i % 2 == 0:
            res += testList[i]
    print(f"сумма четных элементов = {res}")

Summ4etElements(CreateSpisok(n,testList))