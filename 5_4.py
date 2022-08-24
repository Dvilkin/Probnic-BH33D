# Написать программу генерации треугольника паскаля указанной глубины

n: int = int(input('Enter kolicestvo yrovnei treygolnika:'))
treygolnik = []
for i in range(n):
    treygolnik.append([1] + [0] * n)
for i in range(1, n):
    for j in range(1, n):
        treygolnik[i][j] = treygolnik[i - 1][j] + treygolnik[i - 1][j - 1]
for i in range(0, n):
    for j in range(0, n):
        print(treygolnik[i][j], end=' ')
    print()
