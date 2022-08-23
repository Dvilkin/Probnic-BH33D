#Вводится строка, вывести уникальные символы

stroka = input("Enter stroky:")
for x in set(stroka):
    if stroka.count(x) == 1:
        print(x)

