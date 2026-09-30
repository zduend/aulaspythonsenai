menu = int(input("digite o código do item: "))
match menu:
    case 1:
        print("Produto:Cachorro quente")
        print("Valor:R$ 10,00")
    case 2:
        print("Hambúrguer")
        print("R$ 15,00")
    case 3:
        print("Batata Frita")
        print("Valor:R$ R$ 8,00")
    case 4:
        print("Refrigerante")
        print("Valor:R$ R$ 5,00")
    case _:
        print("Código inválido")