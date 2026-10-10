import requests
import json

#REQUISIÇÃO GET
link = 'http://192.168.205.100:8080/usuarios'
resposta = requests.get(link)
print(f"STATUS BUSCA DADOS: {resposta}")


#RESIÇÕES POST = enviar
#chaves aceitas na API da aula: 'nome', 'email'
meus_dados ={
    'nome': 'Samuel',
    'email': 'mono_trynda@senai.com',
}

envio = requests.post(link, json=meus_dados)
print(envio)

resposta = requests.get(link+'/1')
print(f'STATUS BUSCA DADOS POR ID: {resposta.json()}')

#REQUISIÇÃO PUT = alterar
dado_atualizado = {
    'nome': 'Samuel',
    'email': '',
}

atualizacao = requests.put((link+'/1'), json=meus_dados)
print(atualizacao)

#REQUISIÇÃO DELETE = exluir
deletar = requests.delete(link+'/1')
print(f"status: {deletar}")


eniando_dados_aleatorios = requests.post(link, json=novo_dado)
print(eniando_dados_aleatorios.json())


#=============================================================================

busca_cep = requests.post(link_cep)
busca_pessoa =
