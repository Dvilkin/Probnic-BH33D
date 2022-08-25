# Дан список чисел, отсортировать его по возрастанию без использования sort и sorted

spisok_cisel = list(map(int, input('Enter celie cisla cherez probel:').split()))
print(spisok_cisel)
for all_element in range(len(spisok_cisel) - 1):
    for i in range(len(spisok_cisel) - 1 - all_element):
        if spisok_cisel[i] > spisok_cisel[i + 1]:
            spisok_cisel[i], spisok_cisel[i + 1] = spisok_cisel[i + 1], spisok_cisel[i]
print(spisok_cisel)
