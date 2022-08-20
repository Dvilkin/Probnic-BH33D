# Без использования collections, написать программу, которая будет создавать словарь
# для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры


stroka: str = str(input('Введите строку:'))
dlina = len(stroka)
print(len(stroka))
s = stroka[:]
print(s)
list = {n: (stroka[n]) for n in range(0, dlina)}
print(list)
