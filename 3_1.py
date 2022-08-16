# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

#способ №1
stroka = input('Введите сторку 1:')
stroka = stroka.replace(' ', '-')
print(stroka)

#способ №2
stroka = input('Введите сторку 2:')
stroka = stroka.split()
stroka = '-'.join(stroka)
print(stroka)
