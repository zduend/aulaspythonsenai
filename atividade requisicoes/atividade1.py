import json
import requests


while True:
    cep = input('Digite o cep: ')
    link = f'https://viacep.com.br/ws/{cep}/json/'
    resposta = requests.get(link)
    if resposta.status_code == 200:
        print(resposta.json())


    dicionario_dados_cep = []
    dicionario_dados_cep.append(resposta.json())


    for dicionario in dicionario_dados_cep:
        print(f"{dicionario['logradouro']}\n"
              f" {dicionario['localidade']}\n"
              f" {dicionario['cidade']}\n")

    with open('dados.json', 'w', encoding='utf8') as arquivo:
        json.dump(resposta.json(), arquivo, ensure_ascii=False, indent=4)
