import json

loja = {
    "nome": "SamucaStore",
    "produtos":[
        {"nome":"Teclado", "preco": 50, "quantidade": 100},
        {"nome":"Mouse", "preco": 25, "quantidade": 200},
        {"nome":"Monitor", "preco": 300, "quantidade": 70},
    ]
}

with open('estoque.json', 'w',encoding = 'utf-8') as arquivo:
    json.dump(loja, arquivo, ensure_ascii=False,indent=4)

with open('estoque.json', 'r',encoding = 'utf-8') as arquivo:
    dados_lidos = json.load(arquivo)

for produto in dados_lidos['produtos']:
    print(f"O produto {produto['nome']} Custa - R${produto['preco']:.2f}")

novo_produto = {
        "nome": "Fone",
        "preco": 120,
        "quantidade": 80
    }
dados_lidos['produtos'].append(novo_produto)

print(dados_lidos['produtos'])
