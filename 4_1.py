# Заполнить список степенями числа 2 (от 2^1 до 2^n)

n: int = int(input('Введите сепень числа 2:'))
for i in range(1, n + 1):
    print(2 ** i)

list = [i for i in range(1, n + 1)]
print(list)

# for i in range(1,n):
#     print(2**i)
