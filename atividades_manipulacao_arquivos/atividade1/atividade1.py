usuario = input('Digite seu nome para iniciar a compra: ')
produtos = []

while True:
    descricao_produto = input('Digite o nome do produto ou fim para sair: ')
    if descricao_produto == 'fim':
        break
    else:
        preco_produto = float(input("Digite o preço do produto: "))
        produtos.append([descricao_produto, preco_produto])

total = 0
for produto in produtos:
    total = total + produto[1]

with open("pagamento.txt", "w") as arquivo:
    arquivo.write("RECIBO DE COMPRA\n")
    arquivo.write(f"nome do cliente: {usuario}\n")
    arquivo.write(f"Lista detalhada de produtos:\n")

    for item in produtos:
        arquivo.write(f"{item[0]} - R$ {item[1]:.2f}\n")

    arquivo.write(f"total da compra: {total:.2f}\n")

with open("pagamento.txt", "r") as arquivo:

    print("\n--- FINALIZANDO COMPRA ---")

    conteudo = arquivo.read()
    posicao = conteudo.find("total da compra: ")
    inicio = posicao + len("total da compra: ")
    valor_total = conteudo[inicio:]

    print("\n--- PROCESSANDO PAGAMENTO ---")

    print(f"Compra processada com sucesso! Valor cobrado: R${valor_total}")






