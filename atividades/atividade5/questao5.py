real1 = int(input("Digite o primeiro numero: "))
real2 = int(input("Digite o segundo numero: "))
operador = input("Digite o operador matemático: ")
match operador:
    case "+":
        print(real1 + real2)
    case "-":
        print(real1 - real2)
    case "*":
        print(real1 * real2)
    case "/":
        print(real1 / real2)
    case _:
        print("Operador invalido!")
