# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print("ВВЕДИТЕ НОМЕР ЧЕТВЕРТИ: ")

n = 0
while n < 1 or n > 4:
        n = int(input())
        if n < 1 or n > 4:
            print("НЕКОРЕКТНЫЙ ВВОД")
            print("ВВЕДИТЕ ПРАВИЛЬНОЕ ЧИСЛО")
        else:
            if n == 1:
                print("X --> от 0 до + ꝏ")
                print("Y --> от 0 до + ꝏ")
            elif n == 2:
                print("X --> от 0 до + ꝏ")
                print("Y --> от 0 до - ꝏ")
            elif n == 3:
                print("X --> от 0 до - ꝏ")
                print("Y --> от 0 до - ꝏ")
            else:
                print("X --> от 0 до - ꝏ")
                print("Y --> от 0 до + ꝏ")               
            

    


