# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

chislo_1: float = float(input('Введите число 1:'))
chislo_2: float = float(input('Введите число 2:'))
chislo_3: float = float(input('Введите число 3:'))
sr_arifmeticheckoe = float((chislo_1+chislo_2+chislo_3)/3)
print('Среднее арифмитическое =', round(sr_arifmeticheckoe, 3))
