def media ():
    nome_aluno = input("Digite o nome do aluno:")
    nota_1 = float(input("Digite a nota do primeiro bimestre:"))
    nota_2 = float(input("Digite a nota do segundo bimestre:"))
    nota_3= float(input("Digite a nota do terceiro bimestre:"))
    nota_4 = float(input("Digite a nota do quarto bimestre:"))
    calculo_media = (nota_1 + nota_2 + nota_3 + nota_4) /4
    if calculo_media >=7:
        print(f"{nome_aluno}, sua média foi {calculo_media} você está aprovado.")
    else:
        print(f"{nome_aluno}, sua média foi {calculo_media} você está reprovado.")
media()
