
# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_number = int(input())
if day_number < 6:
    print("нет")
elif day_number <= 7 and day_number >= 6 :
    print("Ура выходной!!!")
else:
    print("вы ввели какую-то безлепицу")