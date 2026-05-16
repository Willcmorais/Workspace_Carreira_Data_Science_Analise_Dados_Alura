# 4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

aluguel = [
    ("Apartamento", 1700),
    ("Apartamento", 1400),
    ("Casa", 2150),
    ("Apartamento", 1900),
    ("Casa", 1100),
]


def extrair_valor_numerico():
    valor_numerico = [i[1] for i in aluguel if i[0] == "Apartamento"]
    return valor_numerico


def main():
    val_num = extrair_valor_numerico()
    print(val_num)

    print(
        "List Comprehension dos valores númericos de cada tupla cujo primeiro elemento foi 'Apartamento':"
    )
    for i in val_num:
        print(i)


if __name__ == "__main__":
    main()
