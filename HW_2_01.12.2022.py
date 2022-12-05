# 2'. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]


from os import system 
system("cls")

Mnozheteli = []
i = 1
# condition_1  = (i%2)==0 and (i/2)>1  ----- МОЖНО ЛИ ТАКОЕ ПИХАТЬ В IF ???
n = input("введите число: ")
if n.isdigit() == True:
    n = int(n)
    tmp = []
    for i in range(1,n+1):
        if (i%2)==0 and (i/2)>1 or ((i%3)==0 and (i/3)>1) or ((i%5)==0 and (i/5)>1) or ((i%7)==0 and (i/7)>1):
            continue
        elif n % i ==0:
            Mnozheteli.append(i)
    print(Mnozheteli, "простые делители")
else:
    print(f"ВЫ ВВЕЛИ --- {type(n)}")

