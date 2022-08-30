# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётные

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 66, 77, 80]
spisok_chetnix = list(filter(lambda x: x % 2 == 0, spisok))
spisok_nechetnix = list(filter(lambda x: x % 2 != 0, spisok))
spisok = spisok_chetnix + spisok_nechetnix
print(spisok)
