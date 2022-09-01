# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка

spisok_cisel = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2, 1, 50, 100]
len_spiska = len(spisok_cisel)


def foo(len_spiska):
    for n in range(len(spisok_cisel)):
        if n == 0:
            print(spisok_cisel[n], spisok_cisel[-1] + spisok_cisel[n + 1])
        elif n == len(spisok_cisel) - 1:
            print(spisok_cisel[n], spisok_cisel[n - 1] + spisok_cisel[0])
        else:
            print(spisok_cisel[n], spisok_cisel[n - 1] + spisok_cisel[n + 1])


foo(0)
