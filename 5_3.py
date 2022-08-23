# **Вывести четные числа от 2 до N по 5 в строку

n: int = int(input('Enter cisla do:'))
predel = 0
cislo = 0
stroka = 0
while predel < n-1:
    predel += 2
    stroka += 1
    cislo += 2
    if stroka % 5 != 0:
        print(cislo, end=" ")
    else:
        print(cislo, end="\n")
