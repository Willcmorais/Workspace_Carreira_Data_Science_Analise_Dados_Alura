# 7. Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
# O texto exibido ao fim deve ser parecido com: "Nome completo: Ana Silva"

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

nome_completo = list(map(lambda x, y: (x + " " + y).title(), nomes, sobrenomes))

for nome in nome_completo:
    print(f"Nome completo: {nome}")
