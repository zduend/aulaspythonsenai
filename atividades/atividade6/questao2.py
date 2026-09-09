senhafixa = 123
senhausuario = int(input("Digite sua senha: "))
while senhausuario != senhafixa:
    print("Senha incorreta. Tente novamente.")
    senhausuario = int(input("Digite sua senha: "))
    if senhausuario == senhafixa:
        print("Acesso permitido!")

