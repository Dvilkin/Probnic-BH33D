# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n: int = int(input('ENTER n:'))
biblioteka = {
    n: {'NAME': input('ENTER Name:'),
        'EMAIL': input('ENTER email:')} for n in range(1, n + 1)}
print(biblioteka)
