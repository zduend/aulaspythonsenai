import json


with open('banco_livros.txt', 'r', encoding = 'utf-8') as arquivo:
    linhas = arquivo.readlines()

catalogo_livros = []
for linha in linhas:
    dados = linha.strip().split(";")
    livro = {
        "id": int(dados[0]),
        "nome": dados[1],
        "descricao": dados[2],
        "preco": float(dados[3]),
        "em_estoque": int(dados[4]),
    }
    catalogo_livros.append(livro)

with open('catalogo.json', 'w', encoding = 'utf-8') as arquivo:
    json.dump(catalogo_livros, arquivo, ensure_ascii=False, indent=4)

novo_livro = {
    "id": 31,
    "nome": "Biografia de Jesus",
    "descricao": "Teologia",
    "preco": 49.90,
    "em_estoque": 40,
}
catalogo_livros.append(novo_livro)

novo_livro = {
    "id": 32,
    "nome": "Introdução à Python",
    "descricao": "Desenvolvimento",
    "preco": 80.00,
    "em_estoque": 32,
}
catalogo_livros.append(novo_livro)

novo_livro = {
    "id": 33,
    "nome": "Maria e João",
    "descricao": "História",
    "preco": 33.90,
    "em_estoque": 56,
}
catalogo_livros.append(novo_livro)

novo_livro = {
    "id": 34,
    "nome": "O Último Suspiro de Órion",
    "descricao": "Ficção Cientifica",
    "preco": 55.34,
    "em_estoque": 56,
}
catalogo_livros.append(novo_livro)

novo_livro = {
    "id": 35,
    "nome": "A Sombra no Fim do Corredor",
    "descricao": "Mistério",
    "preco": 34.90,
    "em_estoque": 45,
}
catalogo_livros.append(novo_livro)


with open('catalogo.json', 'w', encoding = 'utf-8') as arquivo:
    json.dump(catalogo_livros, arquivo, ensure_ascii=False, indent=4)

with open('catalogo.json', 'r', encoding = 'utf-8') as arquivo:
    dados_lidos = json.load(arquivo)

for livro in dados_lidos:
    if livro["em_estoque"] < 15:
        print(livro["nome"])

valor_total_livros = 0
for livro in dados_lidos:
    valor_total_livros = valor_total_livros + (livro["preco"] * livro["em_estoque"])
    print(f"Valor total do estoque: R$ {valor_total_livros:.2f}")


