# Напишите программу для. 
# проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input())
y = bool(input())
z = bool(input())

a = not(x or y or z)
b = not(x) and not(y) and not(z)

print(a==b)

if a == b:
    print("True")
else:
    print("False")