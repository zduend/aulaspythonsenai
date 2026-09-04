idadedapessoa = int(input("Digite o idade de 15pessoa: "))
possuivip = input("voce possui vip?: ")
validaorganizador = int(input("Você é organizador?: "))
validavip = 1
organizador = 1
if idadedapessoa >= 18 or possuivip == 1 and validaorganizador:
    print("Entrada PERMITIDA! Seja bem-vindo(a)")
else:print("Entrada NEGADA!")