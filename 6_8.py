# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

slovar = {
    "Belarus": ['Minsk', 'Brest', 'Vitebsk', 'Gomel', 'Grodno', 'Mogilev', 1],
    "Russian Federation": ['Moscow', 'St. Petersburg', 'Sevastopol'],
    'Ukraine': ['Kyiv', 'Kharkiv', 'Odessa']
}
print(slovar.values())


def get_key(slovar, value):  # поиск по ключам и значениям
    for k, v in slovar.items():
        for i in v:  # отображает все значения каждого ключа по очереди
            if i == value:  # сравнивает каждое значение с искомым
                return k  # если находит выводит ключ


value = input(f'Enter gorod:')
print(get_key(slovar, value))
