# Вывести первые N цисел кратные M и больше K

n: int = int(input("Enter kolichestvo chisel:"))
m: int = int(input("Enter kratnost chisel:"))
k: int = int(input("Enter bolhe chisla:"))

kol_chisel = 0
while kol_chisel < n:
    if k % m == 0 and k != 0:
        print(k)
        kol_chisel += 1
        k += m
    else:
        k += 1
