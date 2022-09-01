# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

spisik_cisel = [1, 2, 3, 4, 5, 6, 7, 8, 9]
smescenie: int = int(input("Enter smescenie ot 1 do 8:"))


def foo(smescenie):
    spisik = spisik_cisel[-smescenie:] + spisik_cisel[:-smescenie]
    print(spisik)
    return spisik


foo(smescenie)
