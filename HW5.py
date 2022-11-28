# Напишите программу, 
# которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from random import randint

x = randint(-10,10)
y = randint(-10,10)
x1 = randint(-10,10)
y1 = randint(-10,10)

# x = 3  
# y = 6
# x1 = 2
# y1 = 1

rasstoyanie = ((x1-x)*(x1-x) + (y1-y)*(y1-y))**(0.5)
print(round(rasstoyanie, 1))
