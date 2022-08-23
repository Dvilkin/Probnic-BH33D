# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

cislo1: float = float(input("Enter 1-voe chislo:"))
deistvie: str = input("Enter deistvie (+), (-), (*), (/), (%), (**), (//): ")
cislo2: float = float(input("Enter 2-voe chislo:"))
if deistvie == "+":
    print(cislo1 + cislo2)
elif deistvie == "-":
    print(cislo1 - cislo2)
elif deistvie == "*":
    print(cislo1 * cislo2)
elif deistvie == "/":
    print(cislo1 / cislo2)
elif deistvie == "%":
    print(cislo1 % cislo2)
elif deistvie == "**":
    print(cislo1 ** cislo2)
elif deistvie == "//":
    print(cislo1 // cislo2)
