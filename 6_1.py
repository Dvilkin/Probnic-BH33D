# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int

# Перевод в 2-ную систему
n = int(input('Enter chislo v 10-noy sisteme:'))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)

# Перевод в 10-ную систему
n = list(input('Enter chislo v 2-noy sisteme:'))
d = len(n)
f = 0
c = 0
h = 1
for i in range(0, d):
    f += int(n[c]) * (2 ** (d - h))
    c += 1
    h += 1
print(f)
