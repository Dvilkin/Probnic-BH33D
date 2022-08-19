# Заполнить список степенями числа 2 (от 2^1 до 2^n)

n: int = int(input ('Введите сепень n:'))
steneni = [i for i in range(2**1, 2**n)]
print(steneni)
