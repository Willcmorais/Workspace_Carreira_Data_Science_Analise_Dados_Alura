# 6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código. Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.:

vendas = [
    ("2023", 4093),
    ("2021", 4320),
    ("2021", 5959),
    ("2022", 8883),
    ("2023", 9859),
    ("2022", 5141),
    ("2022", 7688),
    ("2022", 9544),
    ("2023", 4794),
    ("2021", 7178),
    ("2022", 3030),
    ("2021", 7471),
    ("2022", 4226),
    ("2022", 8190),
    ("2021", 9680),
    ("2022", 5616),
]


def vendas_2022():
    vendas_geral_2022 = list(filter(lambda x: x[0] == "2022", vendas))

    vendas_2022_acima_6000 = list(filter(lambda x: x[1] > 6000, vendas_geral_2022))

    filtro_apenas_valores_2022_acima_6000 = [
        valor[1] for valor in vendas_2022_acima_6000
    ]

    return filtro_apenas_valores_2022_acima_6000


def main():
    print(f"Vendas em 2022 com valores acima de R$ 6.000,00: \n{vendas_2022()}")


if __name__ == "__main__":
    main()
