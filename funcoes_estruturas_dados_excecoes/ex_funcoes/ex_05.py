# 5. Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

# Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

# "Nota da manobra: [media]"


def nota_manobra():
    notas_manobras = []
    for i in range(5):
        nota_jurado = float(input(f"Informe a {i + 1}ª nota do skatista: "))
        notas_manobras.append(nota_jurado)

    nota_maxima = max(notas_manobras)
    nota_minima = min(notas_manobras)

    notas_manobras.remove(nota_maxima)
    notas_manobras.remove(nota_minima)

    media_skatista = sum(notas_manobras) / len(notas_manobras)

    return media_skatista


resultado = nota_manobra()

print(f"\nNota da manobra: {resultado:.2f}")
