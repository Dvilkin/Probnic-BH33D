# Вводятся две строки, a и b, и возвращать количество раз,
# когда в обеих строках под одинаковыми индексами стоит одна и та же пара букв.

stroka1 = str(input('Enter stroky 1:')).lower()
stroka2 = str(input('Enter stroky 2:')).lower()
prover_simvol = 0
sovpadenie = 0
dlina_stroki1 = len(stroka1)
dlina_stroki2 = len(stroka2)
while prover_simvol < dlina_stroki1 and prover_simvol < dlina_stroki2:
    if stroka1[prover_simvol] == stroka2[prover_simvol] and stroka1[prover_simvol].isalpha():
        print('Sovpadadenie bykvi:', stroka1[prover_simvol])
        prover_simvol += 1
        sovpadenie += 1
        print('Sovpadenie #', sovpadenie)
    else:
        prover_simvol += 1
