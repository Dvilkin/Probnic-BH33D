# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа - пустая строка)

slovar = {
    'id1':
        {'name': 'Oleg',
         'surname': 'Antonovic',
         'tel': 375291234567,
         'email': 'oleg@gmail.com'},
    'id2':
        {'name': 'Alexsandr',
         'surname': 'Igorevic',
         'tel': 375292251289,
         'email': 'alex@gmail.com'},
    'id3':
        {'name': 'Sergey',
         'surname': 'Petrovic',
         'tel': 375298975060,
         'email': None},
    'id4':
        {'name': 'Petr',
         'surname': 'Afanasevic',
         'tel': 375299963080,
         'email': None},
    'id5':
        {'name': 'Georgii',
         'surname': 'Matveevic',
         'tel': 375336587121,
         'email': 'alex@gmail.com'}
}
