# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) 
# -2 -1 0 1 2 Позиции: 0,1 -> 2

from os import system 
from random import randint
system("cls")

n = int(input())
list_N_N = []

def Generate_ot_N_do_N(n):
    for i in range((-n),n+1):
        list_N_N.append(i)
    

def GenerateSpisokInFile(ot_N_do_N):
    fi_le = open("Ftext.txt", "w")

    for i in range(0,len(list_N_N)):
        fi_le.write(str(i)+ "\n") 
    
    fi_le.close()

    fi_le = open("Ftext.txt", "r")
    fi1_le = fi_le.read()
    print(fi1_le)



GenerateSpisokInFile(Generate_ot_N_do_N(n))

print(f" Последовательность от <{-n}> до <{n}> -->{list_N_N}")


fi_le = open("Ftext.txt", "r")
fi1_le = [line.strip() for line in fi_le]
a = randint(0, len(fi1_le))
b = randint(0, len(fi1_le))

print(a, "Это А")
print(b, "Это B")
print(f" произведение от <{list_N_N[a]}> нв <{list_N_N[b]}> -->{list_N_N[a]*list_N_N[b]}")

fi_le.close()




