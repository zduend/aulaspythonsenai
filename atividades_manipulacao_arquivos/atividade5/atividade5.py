with open('banco_livros.txt', 'r', encoding = 'utf-8') as arquivo:
    linhas = arquivo.readlines()
for linha in linhas:
    print(linha.strip())

dados = linhas[0].strip().split(";")

livro = {
    "id": int(dados[0]),
    "nome": dados[1],
    "preco": float(dados[3]),
    "em_estoque": int(dados[4]),

}
print(livro)