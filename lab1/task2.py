from math import cos, log, sin, exp

x = float(input("Введите значение переменной x: "))
y = float(input("Введите значение переменной y: "))
z = float(input("Введите значение переменной z: "))
a=((x**3)/2)**0.5-sin(y)
b=((exp(1)**2)/3)-cos(y)+z+log(y)

print(a)
print(b)
print(f"Получено значение функции a={a}")
