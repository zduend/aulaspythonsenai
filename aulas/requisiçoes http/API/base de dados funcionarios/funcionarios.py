import requests
import json

link_funcionarios = "http://192.168.205.100:8080/funcionarios"

#                json    python
# dados vazios = null == None

resposta = requests.get(link_funcionarios) # enviando uma requisição do tipo GET
print(resposta.json()) # mostrando o que recebeu na requisição HTTP

lista_funcionarios = resposta.json()

print("--- LISTA DE FUNCIONARIOS SEM ENDEREÇO CADASTRADO ---\n")

for funcionario in lista_funcionarios:

    if funcionario['cep'] == None:
        print(f"O funcionário(a) {funcionario['nome']} não tem cep cadastrado\n")

        while True:
            try:
                cep_digitado = input("Digite o CEP dele: ")
                link_cep = f"https://viacep.com.br/ws/{cep_digitado}/json/"
                resposta = requests.get(link_cep)
                print(resposta.status_code)

                if resposta.status_code == 200:
                    dicionario_funcionario = resposta.json()

                    funcionario['cep'] = dicionario_funcionario['cep']
                    funcionario['cidade'] = dicionario_funcionario['localidade']
                    funcionario['estado'] = dicionario_funcionario['estado']
                    break
                else:
                    print("cep digitado incorretamente")
            except Exception as erro:
                print("Erro ao obter o CEP NAO TEM ENDEREÇO")


# base de dados atualizada
for funcionario in lista_funcionarios:
    print(funcionario)


with open('funcionarios.json', 'w',encoding='utf-8') as json_file:
    json.dump(lista_funcionarios, json_file, ensure_ascii=False, indent=4)



# inserir dados onde estiver algum dado vazio
# no cep, apenas aceitar CEPS válidos
#   (que tenham retorno de cidade, estado, etc...)
# salvar os dados preenchidos em um arquivo JSON
#   (ex: dados_funcionarios_atualizados.json)