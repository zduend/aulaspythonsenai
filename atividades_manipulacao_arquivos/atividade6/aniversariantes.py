import json

with open("dados1.json", 'r', encoding = 'utf-8') as arquivo:
    dados1 = json.load(arquivo)

with open("dados2.json", 'r', encoding = 'utf-8') as arquivo:
    dados2 = json.load(arquivo)

with open("dados3.json", 'r', encoding = 'utf-8') as arquivo:
    dados3 = json.load(arquivo)

lista_aniversariantes = []
for aniversariante in dados1:
    funcionario = {
        'nome': aniversariante['nome'],
        'aniversario': aniversariante['aniversario'],
    }
    lista_aniversariantes.append(funcionario)

for aniversariante in dados2:
    funcionario = {
        'nome': aniversariante['nome'],
        'aniversario': aniversariante['aniversario'],
    }
    lista_aniversariantes.append(funcionario)

for aniversariante in dados3:
    funcionario = {
        'nome': aniversariante['nome'],
        'aniversario': aniversariante['aniversario'],
    }
    lista_aniversariantes.append(funcionario)

lista_aniversariantes = sorted(lista_aniversariantes, key = lambda x: x['nome'],)

with open('aniversariantes.json', 'w', encoding = 'utf-8') as arquivo:
    json.dump(lista_aniversariantes, arquivo, ensure_ascii = False, indent = 4)

for aniversariante in lista_aniversariantes:
    print(f"Nome: {aniversariante['nome']} | Aniversario: {aniversariante['aniversario']}")

print(f'Total de aniversariantes: {len(lista_aniversariantes)}')