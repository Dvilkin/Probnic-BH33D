# Код Морзе для представления цифр и букв использует тире и точки. Напишите
# функцию для кодирования текстового сообщения в соответствии с кодом Морзе.
# (словари в помощь)

morse = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••',
         'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•',
         's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••',
         '1': '•————', '2': '••———', '3': '•••——', '4': '••••—', '5': '•••••', '6': '—••••', '7': '——•••',
         '8': '———••', '9': '————•', '0': '—————'}

a = input("Enter text:")


def Morse(s):
    a = ''
    for i in s.lower():
        if i in morse.keys(): a += morse[i] + ' '
        if i == ' ': a += ' / '  # Слова разделяются слэшем
    return a


def get_key(val, dct):  # Функция возвращает ключ словаря по значению
    for key, value in dct.items():
        if val == value: return key


def MorseTxt(s):
    a, s = '', s.split()
    for i in s:
        if i in morse.values(): a += get_key(i, morse)
        if i == '/': a += ' '
    return a


print(Morse(a))
print(MorseTxt(Morse(a)))
