# Без использования collections, написать программу, которая будет создавать словарь
# для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

# dlina = len(stroka)
# print(len(stroka))
# list = {n: (stroka[n]) for n in range(0, dlina)}
# print(list)
# list2 = [(stroka[n]) for n in range(0, dlina)]
# print(list2)
# list3 = list2.count((stroka(n)) for n in range(0, dlina))
# print(list3)
stroka: str = str(input('Введите текст:'))
dlina = len(stroka)
print(len(stroka))
kol_bykv = {
    stroka[0]
}
print(kol_bykv)
