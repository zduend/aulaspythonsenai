nomedoproduto = input("Digite o nome do produto: ")
custodefabrica = float(input("Digite o valor do custo: "))
precovenda = float(input("Digite o valor do preco na loja: "))
calculolucro = precovenda - custodefabrica
validalucro = calculolucro > 20
print("Nome do produto: ",nomedoproduto,)
print("Lucro Obtido:", calculolucro)
print("O lucro foi bom?:", validalucro)
