# 3. A partir da lista abaixo, crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

lista = ["Pedro", "Júlia", "Otávio", "Eduardo"]


def zip_de_listas():
    zip_indice_nome = list(zip([i for i in range(len(lista))], lista))
    return zip_indice_nome


def main():
    tuplas = zip_de_listas()
    print(tuplas)

    print("lista de tuplas com o índice e o nome ordenado:")
    for i in tuplas:
        print(i)


if __name__ == "__main__":
    main()
