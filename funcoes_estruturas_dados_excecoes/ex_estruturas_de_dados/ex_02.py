# 2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

lista_de_tuplas = [("Pedro", 1.74, 81), ("Júlia", 1.65, 67), ("Otávio", 1.81, 83)]


def terceiro_elemento():
    elemento_tres = [elemento[2] for elemento in lista_de_tuplas]
    return elemento_tres


def main():
    elemento = terceiro_elemento()
    print(elemento)
    print("Terceiro elemento de cada tupla:")
    for i in elemento:
        print(i)


if __name__ == "__main__":
    main()
