import json
import requests
cep = input('Digite o cep: ')
link = f'https://viacep.com.br/ws/{cep}/json/'
resposta = requests.get(link)
if resposta.status_code == 200:
    print(resposta.json())

with open('dados.json', 'w', encoding='utf8') as arquivo:
    json.dump(resposta.json(), arquivo, ensure_ascii=False, indent=4)