# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка незаконно

spisok = [1, 2, 3, 'Leto', [89, 90, 91, 92], 'osen blizko', True, None]
rez = list(filter(lambda x: x.isalpha(), spisok))
print(rez)


# def filter_slov(n):
#     if spisok[:] == str:
#         print(spisok[:])
#         return


# dlina_spiska = len(spisok)
# spisok.sort()
# print(dlina_spiska)
# print(spisok)
# for i in range(0, dlina_spiska-1):
#     if i != str:
#         del spisok[i]
# print(spisok)
