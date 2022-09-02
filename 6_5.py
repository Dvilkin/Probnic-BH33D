# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза

my_range = [1, 2, 3, 50, 89, 21, 30, 8]
print(type(my_range))


def perevorot(ert):
    for i in my_range:
        my_range += my_range[-1]
    return my_range


my_range = perevorot(my_range)
print(my_range)
