lista_funcionarios = []
numero_funcionarios = 0
lista_aumento = []
lista_demitidos = []



while True:
    funcionario = input("Adicione um funcionario: ")
    lista_funcionarios.append(funcionario)

    opcao = input("Deseja continuar? [S/N] ")
    if opcao == "N":
        break
print(lista_funcionarios)

for index in range(0, len(lista_funcionarios)):
    print([index],[lista_funcionarios[index]])

while True:
    index_aumento = int(input("Digite o índice do funcionário que receberá aumento:"))
    lista_aumento.append(lista_funcionarios[index_aumento])
    opcao = input("Deseja escolher outro? [S/N] ")
    if opcao == "N":
        break

while True:
    index_demissao = int(input("Digite o indice de quem será demitido: "))
    lista_demitidos.append(lista_funcionarios[index_demissao])
    opcao = input("Deseja escolher outro? [S/N] ")
    if opcao == "N":
        break

for index in range(0, len(lista_aumento)):
    print("Este Funcionario terá aumento: ", [index],[lista_aumento[index]])

for index in range(0, len(lista_demitidos)):
    print("Este Funcionário será demitido: ", [index],[lista_demitidos[index]])



