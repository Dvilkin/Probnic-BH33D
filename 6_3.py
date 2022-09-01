# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]

spisik_cisel = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def foo(smescenie):
    spisok = spisik_cisel[-smescenie:] + spisik_cisel[:-smescenie]
    return spisok


spisok = foo(
    int(input(f'Enter smescenie ot 1 do 8:')))  # Вводим смежение и присваиваем переменной результат работы функции
print(spisok)
