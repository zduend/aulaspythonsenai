produtos = []
produtos_retirados = []

while True:
    produto = input("Digite o nome do produto: ")
    produtos.append(produto)
    opcao = input("Deseja continuar? [S/N] ")
    if opcao.upper() == "N":
        break
for index in range(0, len(produtos)):
    print([index], produtos[index])

while True:
    opcao = input("Deseja retirar algum produto? [S/N] ")
    if opcao.upper() == "N":
        break
    exclusao = int(input("Digite o índice do produto retirado: "))
    produtos_retirados.append(produtos[exclusao])

print(f"Lista de produtos: {produtos}")
print(f"lista de produtos retirados: {produtos_retirados}")
