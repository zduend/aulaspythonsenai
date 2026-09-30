saldodispo = float(input("Digite o saldo atual: "))
valordesejadosacar = float(input("Digite o valor que deseja sacar: "))
if valordesejadosacar <= saldodispo:
    subtracao = valordesejadosacar % saldodispo
    print("Saque realizado com sucesso","Saldo atualizado:", subtracao)

else:print("Saldo insuficiente para realizar esta operação")