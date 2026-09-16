lista_alunos = []
while True:
    aluno = input("Adicione um aluno: ")
    lista_alunos.append(aluno)
    opcao = input("deseja continuar? [S/N] ")
    if opcao.upper() == "N":
        break

for index in range(0, len(lista_alunos)):
    print([index], lista_alunos[index])


