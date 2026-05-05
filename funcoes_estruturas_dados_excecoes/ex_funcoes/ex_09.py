# 9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

# O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

# Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

DIARIA_HOTEL = 150
VAL_GASOLINA_LITRO = 5
KM_POR_LITRO_GASOLINA = 14
GASTOS_DIARIOS = {"salvador": 200, "fortaleza": 400, "natal": 250, "aracaju": 300}
DISTANCIA_KM_REC_CIDADES = {
    "salvador": 850,
    "fortaleza": 800,
    "natal": 300,
    "aracaju": 550,
}
dias_de_viagem = 3


def gastos_hotel():
    gastos_hotel = DIARIA_HOTEL * dias_de_viagem
    return gastos_hotel


def gastos_gasolina():
    gastos_gasolina = (
        DISTANCIA_KM_REC_CIDADES["salvador"] * 2 / KM_POR_LITRO_GASOLINA
    ) * VAL_GASOLINA_LITRO
    return gastos_gasolina


def gastos_passeio():
    gastos_passeio = GASTOS_DIARIOS["salvador"] * dias_de_viagem
    return gastos_passeio


despesa_hotel = gastos_hotel()
despesa_gasolina = gastos_gasolina()
despesa_passeio = gastos_passeio()

print("---- DESPESA GERAL VIAGEM RECIFE-SALVADOR(IDA E VOLTA) ----")
print(f"Gastos hotel: R${despesa_hotel:.2f}")
print(f"Gastos gasolina: R${despesa_gasolina:.2f}")
print(f"Gastos passeios: R${despesa_passeio:.2f}")
