n = int(input())

suma = 0

while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10

print("Сумма:", suma)
