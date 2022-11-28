# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

from os import system # это я в гугле подглядел
system("cls")

res = 0
n = input()

try:
    test = float(n)
    print("Это число")
    for i in n:
        if i.isdigit():
            print(i)
            res += int(i)
    print(f"сумма цифр в числе {n} --> {res}")
except ValueError:
    print("Это не число")
