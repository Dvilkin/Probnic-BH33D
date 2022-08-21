# Без использования collections, написать программу, которая будет создавать словарь
# для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

stroka: str = str(input('Введите текст:'))
dlina = len(stroka)
print(len(stroka))
# list = {n: (stroka[n]) for n in range(0, dlina)}
# print(list)
# list2 = [(stroka[n]) for n in range(0, dlina)]
# print(list2)
n = int(0)
print(n)
list_vse = {
    stroka[n]: stroka.count(n) for n in range(0, dlina-1)
}
print(list_vse)

# list3 = list2.count((stroka(n)) for n in range(0, dlina))

#
# dlina = len(stroka)
# print(len(stroka))
# kol_bykv = {
#     stroka[n]:
# }
# print(kol_bykv)
