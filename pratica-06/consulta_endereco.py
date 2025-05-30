"""Desenvolva um programa que consulte informações de
endereço a partir de um CEP fornecido pelo usuário,
utilizando a API ViaCEP. O programa deve exibir o
logradouro, bairro, cidade e estado correspondentes ao CEP
consultado."""

import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    dados = resposta.json()

    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("Endereço encontrado:")
        print("Logradouro:", dados.get("logradouro", "N/A"))
        print("Bairro:", dados.get("bairro", "N/A"))
        print("Cidade:", dados.get("localidade", "N/A"))
        print("Estado:", dados.get("uf", "N/A"))

# Solicita o CEP ao usuário e chama a função
cep_usuario = input("Digite o CEP (somente números): ")
consultar_cep(cep_usuario)