# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# print("ВВЕДИТЕ НОМЕР ЧЕТВЕРТИ: ")

# nw = 0
# while nw < 1 or nw > 4:
#         nw = int(input())
#         if n < 1 or n > 4:
#             print("НЕКОРЕКТНЫЙ ВВОД")
#             print("ВВЕДИТЕ ПРАВИЛЬНОЕ ЧИСЛО")
#         else:
#             if nw == 1:
#                 print("X --> от 0 до + ꝏ")
#                 print("Y --> от 0 до + ꝏ")
#             elif nw == 2:
#                 print("X --> от 0 до + ꝏ")
#                 print("Y --> от 0 до - ꝏ")
#             elif nw == 3:
#                 print("X --> от 0 до - ꝏ")
#                 print("Y --> от 0 до - ꝏ")
#             else:
#                 print("X --> от 0 до - ꝏ")
#                 print("Y --> от 0 до + ꝏ")               
from os import system 
system("cls")

command = input("ВВЕДИТЕ НОМЕР ЧЕТВЕРТИ: ")
match command.split():
    case ["1"]: print("X --> от 0 до + ꝏ; Y --> от 0 до + ꝏ")  
    case ["2"]: print("X --> от 0 до + ꝏ; Y --> от 0 до - ꝏ")
    case ["3"]: print("X --> от 0 до - ꝏ; Y --> от 0 до - ꝏ")
    case ["4"]: print("X --> от 0 до - ꝏ; Y --> от 0 до + ꝏ")
    case unknown_command: print (f"Command '{command}' not understood")

        

    



