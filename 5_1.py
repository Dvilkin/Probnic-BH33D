# Вывести первые N цисел кратные M и больше K

n: int = int(input("Enter kolichestvo chisel:"))
m: int = int(input("Enter kratnost chisel:"))
k: int = int(input("Enter bolhe chisla:"))
chisla = 0
kol_chisel = 0
while kol_chisel <= n:
    if k % m == 0:
        print(round(k::m))
    k += 1
    if
