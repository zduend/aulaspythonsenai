

#################-ADICIONAR ALUNO-###############
def adicionar_aluno():
    nome = input('Digite o nome do aluno: ')
    turma = input('Digite a turma do aluno: ')
    try:
        nota1 = float(input('Digite a primeira nota do aluno: '))
        nota2 = float(input('Digite a segunda nota do aluno: '))
        nota3 = float(input('Digite a terceira nota do aluno: '))
        nota4 = float(input('Digite a quarta nota do aluno: '))
        media = (nota1 + nota2 + nota3 + nota4) / 4
    except ValueError:
        print("Erro! As notas devem ser números. ")
        return


    if media >= 7:
        status = 'Aprovado'
    else:
        status = 'Reprovado'

    print(f"Aluno: {nome} Media: {media:.2f} Status: {status}")

    with open('alunos.txt', 'a', encoding = 'utf-8') as arquivo:
        arquivo.write(f"{nome};{turma};{nota1};{nota2};{nota3};{nota4};{status}\n")


############### CALCULAR MÉDIA ###########################################
def calcular_media():
    nome_busca = input('Digite o nome do aluno: ')

    try:

        with open('alunos.txt', 'r', encoding = 'utf-8') as arquivo:
            alunos = arquivo.readlines()

        encontrado = False

        for aluno in alunos:
            dados = aluno.strip().split(";")
            if len(dados) < 7:
                continue

            if(dados[0] == nome_busca):
                print(f"Aluno Encontrado: {dados[0]}")
                encontrado = True
                nota1 = float(dados[2])
                nota2 = float(dados[3])
                nota3 = float(dados[4])
                nota4 = float(dados[5])
                media = (nota1 + nota2 + nota3 + nota4) / 4
                print(f"A media do aluno {dados[0]} é {media:.2f}")
                break
        if encontrado == False:
            raise ValueError("Aluno não encontrado")

    except ValueError as erro:
        print(erro)

    except FileNotFoundError:
        print("Arquivo alunos.txt não encontrado!")



################## CONSULTAR STATUS #########################################
def consultar_status():
    nome_busca = input('Digite o nome do aluno: ')

    try:
        with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
            alunos = arquivo.readlines()

        encontrado = False

        for aluno in alunos:
            dados = aluno.strip().split(";")
            if len(dados) < 7:
                continue

            if dados[0] == nome_busca:
                encontrado = True
                print(f"Status de aprovação do Aluno {dados[0]} é: {dados[6]}")
                break

        if encontrado == False:
            raise ValueError("Aluno não encontrado")

    except ValueError as erro:
        print(erro)

    except FileNotFoundError:
        print("Arquivo alunos.txt não encontrado!")

################### MOSTRAR MAIOR MÉDIA DA TURMA #################################

def maior_media_turma():
    turma_busca = input('Digite a turma: ')
    try:
        with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
            alunos = arquivo.readlines()
            encontrado = False
            maior_media = -1
            nome_melhor_aluno = ""

            for aluno in alunos:
                dados = aluno.strip().split(";")

                if len(dados) < 7:
                    continue

                if(dados[1] == turma_busca):
                    encontrado = True
                    nota1 = float(dados[2])
                    nota2 = float(dados[3])
                    nota3 = float(dados[4])
                    nota4 = float(dados[5])
                    media = (nota1 + nota2 + nota3 + nota4) / 4
                    print(f"Aluno: {dados[0]} Media: {media:.2f}")

                    if media > maior_media:
                        maior_media = media
                        nome_melhor_aluno = dados[0]

            if encontrado == True:
                print(f"Aluno Com a Maior média: {nome_melhor_aluno}")
                print(f"Maior média: {maior_media:.2f}")
            else:
                print("Nenhum aluno encontrado")

    except FileNotFoundError:
        print("Arquivo alunos.txt não encontrado!")

############################### MENU ####################################
while True:
    print("1 - Adicionar um aluno")
    print("2 - Calcular média de um aluno")
    print("3 - Consultar status de aprovação")
    print("4 - Mostrar a maior média da turma")
    print("5 - Sair")

    try:
        opcao = int(input("Digite uma opção: "))
    except ValueError:
        print("Opção inválida! Digite um número de 1 a 5.")
        continue

    if opcao == 5:
        break
    elif opcao == 1:
        adicionar_aluno()
    elif opcao == 2:
        calcular_media()
    elif opcao == 3:
        consultar_status()
    elif opcao == 4:
        maior_media_turma()

