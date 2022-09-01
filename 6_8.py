# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

slovar = {
    "Belarus": ['Minsk', 'Brest', 'Vitebsk', 'Gomel', 'Grodno', 'Mogilev', 1],
    "Russian Federation": ['Moscow', 'St. Petersburg', 'Sevastopol'],
    'rm': 2
}
print(slovar.values())


def get_key(slovar, value):
    for k, v in slovar.items():
        if v == value:
            return k


print(get_key(slovar, ['Moscow', 'St. Petersburg', 'Sevastopol']))
