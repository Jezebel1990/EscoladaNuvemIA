"""
Crie um programa que consulte a cotação atual de uma
moeda estrangeira em relação ao Real Brasileiro (BRL). O
usuário deve informar o código da moeda desejada (ex: USD,
EUR, GBP), e o programa deve exibir o valor atual, máximo e
mínimo da cotação, além da data e hora da última
atualização. Utilize a API da AwesomeAPI para obter os
dados de cotação.
"""

import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    dados = resposta.json()

    chave = moeda + "BRL"
    if chave in dados:
        info = dados[chave]
        print(f"Cotação {moeda}/BRL:")
        print("Valor Atual:", info["bid"])
        print("Máximo do Dia:", info["high"])
        print("Mínimo do Dia:", info["low"])
        print("Data e Hora da Última Atualização:", info["create_date"])
    else:
        print("Moeda não encontrada ou código inválido.")

# Solicita o código da moeda e chama a função
codigo = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(codigo)
