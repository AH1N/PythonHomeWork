# 4.Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

#     k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
#     k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'. Даны два файла, в каждом из которых находится запись многочлена. 

from random import randint
from os import system 
system("cls")

MnogoCHLEN = ""
k = int(input(" ВВЕДИТЕ СТЕПЕНЬ МНОГОЧЛЕНА:  "))
koeficient = 0


def CHLEN(koeficient,stepen):
    if stepen == 1:
        stepen = ""
    else:
        stepen = "**"+str(stepen)
    if koeficient == 0:
        Virazhenie = ""
    elif koeficient == -1:
        Virazhenie = " " + "-" + "X" + str(stepen)  
    elif koeficient == 1 :
        Virazhenie = " " + "+" + "X" + str(stepen)
    elif koeficient > 1:
        Virazhenie = " " + "+" + str(koeficient) + "X"+ str(stepen)
    else: 
        Virazhenie = " " + str(koeficient) + "X"+ str(stepen)

    return Virazhenie



def CreateMnogochlen():
    MnogoCHLEN = ""
    for i in range(k,0,-1):
        koeficient = randint(-5, 6)
        MnogoCHLEN += CHLEN(koeficient,i)
    if MnogoCHLEN[1] == "+":
        MnogoCHLEN = MnogoCHLEN[2:] +" "+ "+" + " "+str(koeficient)+" " + "= 0"
        print(MnogoCHLEN)
    else:
        MnogoCHLEN = MnogoCHLEN +" "+ "+" + " "+str(koeficient)+" " + "= 0"
        print(MnogoCHLEN)
    return MnogoCHLEN
                          


CreateMnogochlen()

