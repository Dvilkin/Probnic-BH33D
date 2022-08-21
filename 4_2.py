# Без использования collections, написать программу, которая будет создавать словарь
# для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры

stroka: str = str(input('Enter text:'))
dlina = len(stroka)
print('Kolichestvo vvedenix simvolov:', len(stroka))
list_vse = {
    stroka[n]: stroka.count(stroka[n]) for n in range(0, dlina)
}
print(list_vse)
