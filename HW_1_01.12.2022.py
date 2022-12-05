# 1'. Вычислить число Пи c заданной точностью d

# *Пример:* 

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

import math

from os import system 
system("cls")

import math

py = str(math.pi)
d = input("ВВЕДИТЕ ПОРЯДОК ТОЧНОСТИ d: ")
d = len(d) - 2
print(py[:1] + "." + py[2:d+2])

