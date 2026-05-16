# 1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]


def soma_lista_de_listas():
    soma = [sum(i) for i in lista_de_listas]
    return soma


def main():
    somas = soma_lista_de_listas()
    print(somas)
    print("A soma das iteraveis de cada lista:")
    for soma in somas:
        print(soma)


if __name__ == "__main__":
    main()
