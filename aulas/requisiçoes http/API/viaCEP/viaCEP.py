import requests
cep
link = 'viacep.com.br/ws/{}/json/'
resposta = requests.get(link)
print(resposta)

