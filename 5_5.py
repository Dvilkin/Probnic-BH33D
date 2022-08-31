# Дан список строк, наобходимо реализовать пагинатор:
# Если пользователь вводит ">" то выводится следующий  элемент из списка,
# если вводит пользователь "<" то предыдущий по этому списку,
# а так же предусмотреть, что если пользователь сейчас находится на последнем элементе,
# то следующий это первый, а если находится на первом элементе, то предыдущий это последний,
# чтобы пользователь мог прокручивать список по кругу в любом направлении

objects = ['john', 'paul', 'george', 'ringo']
count_list = 0
print('Enter next > back < current selection:', objects[count_list])
while 1:
    zapros = input()
    if zapros == '>':
        count_list += 1
        if zapros == len(objects):
            zapros = 0
        print('Enter next > back < current selection:', objects[count_list])
        continue
    elif zapros == '<':
        if count_list == 0:
            count_list = len(objects)
        count_list -= 1
        print('Enter next > back < current selection:', objects[count_list])
        continue
