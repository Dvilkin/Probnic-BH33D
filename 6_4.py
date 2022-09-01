# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка незаконно

spisok = [1, 2, 3, 'Leto', [89, 90, 91, 92], 'osen blizko', True, None]


def foo(spisok_strok):
    spisok_strok = list(filter(lambda x: type(x) == str, spisok))
    return spisok_strok


spisok_strok = foo(input(f'Enter start:'))
print(spisok_strok)
