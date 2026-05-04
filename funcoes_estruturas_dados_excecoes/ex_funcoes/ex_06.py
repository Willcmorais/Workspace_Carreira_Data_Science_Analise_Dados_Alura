# 6. Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

# maior nota
# menor nota
# média
# situação (Aprovado(a) ou Reprovado(a))

# Para testar o comportamento da função, os dados podem ser exibidos em um texto: "O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"


def receber_notas():
    lista_notas = []
    for i in range(4):
        nota = float(input(f"Informe a {i + 1}ª nota: "))
        lista_notas.append(nota)

    maior_nota = max(lista_notas)
    menor_nota = min(lista_notas)
    media_notas = sum(lista_notas) / len(lista_notas)

    if media_notas >= 7:
        situacao = "Aprovado(a)"
    else:
        situacao = "Reprovado(a)"

    return maior_nota, menor_nota, media_notas, situacao


maior_nota, menor_nota, media, situacao = receber_notas()

print(
    f"O(a) estudante obteve uma média de {media:.2f}, com a sua maior nota de {maior_nota} pontos e a menor nota de {menor_nota} pontos e foi {situacao}"
)
