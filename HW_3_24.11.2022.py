#  Задайте список из n чисел последовательности 
# 
# (1+1/n)^n 
# и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} ???????????????????


from os import system 
system("cls")

n = int(input())        

res = 0
summ = 0
for i in range(1,n+1):
    res = round(((1+1/i)**i),3)
    print (f"{i} : {res}", end = "  ")
    summ += res

print(f"** {summ} --- это сумма **")