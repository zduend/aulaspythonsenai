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
print(f"O prduto {novo_produto['nome']} custa R${novo_produto['preco']:.2f}")


print(dados_lidos['produtos'])

for produto in dados_lidos['produtos']:
    if produto['nome'] == "Monitor":
        produto['preco'] = produto['preco'] * 0.90
        print(f"Monitor com 10% de desconto: {produto['preco']:.2f}")

with open('estoque.json', 'w',encoding = 'utf-8') as arquivo:
    json.dump(dados_lidos, arquivo, ensure_ascii=False,indent=4)

