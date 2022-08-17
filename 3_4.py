#Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных

x_1: float = float(input('Введите число 1:'))
x_2: float = float(input('Введите число 2:'))
x_3: float = float(input('Введите число 3:'))
polozitelnix = (x_1>0) + (x_2>0) + (x_3>0)
otricatelnix = 3 - polozitelnix
print("Положительных", polozitelnix)
print("Отрицательных", otricatelnix)
