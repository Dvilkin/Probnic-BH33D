# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

n: int = int(input('ENTER n:'))
name = input('ENTER Name:')
email = input('ENTER email:')
data = {
    'NAME': name,
    'EMAIL': email
}
biblioteka = {
    n: data for n in range(1, n+1)}
print(biblioteka)
print(data)
