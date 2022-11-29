# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
from os import system 
system("cls")

num = int(input())
number = num
binares = ""

while num > 0:
    binares = str(num % 2) + binares
    num = num // 2

print(binares)

print("ИЛИ ЧЕРЕЗ BIN()")
sl = slice(2,len(bin(number)))
print(bin(number)[sl])