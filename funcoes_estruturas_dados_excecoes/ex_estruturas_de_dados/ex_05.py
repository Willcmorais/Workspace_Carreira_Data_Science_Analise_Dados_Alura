# 5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista_meses e os valores estão na lista despesa:

lista_meses = [
    "Jan",
    "Fev",
    "Mar",
    "Abr",
    "Mai",
    "Jun",
    "Jul",
    "Ago",
    "Set",
    "Out",
    "Nov",
    "Dez",
]

despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]


def novo_dicionario():
    novo_dicionario = {lista_meses[i]: despesa[i] for i in range(len(lista_meses))}
    return novo_dicionario


def main():
    novo_dict = novo_dicionario()
    print(novo_dict)
    for chave, valor in novo_dict.items():
        print(f"Mês: {chave} - Despesa: R${valor:.2f}")


if __name__ == "__main__":
    main()
