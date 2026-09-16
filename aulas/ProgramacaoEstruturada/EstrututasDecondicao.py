#IF e ELSE -> SE e SENÃO

#CASE SENSITIVE -> E != e
idade = int(input('Digite sua idade: '))

# criando uma condição na execução do código
if idade >= 18: # executa SE a resposta boleana for True
    if idade > 65:
        print("Desculpa senhor, você não pode entrar nessa balada.")
    else:
        print("Você pode entrar nessa balada.")
elif idade < 5:    # ELSE + IF -> elif
    print("Além de não entrar, você não pode andar sozinho!!!")
else:
    print("Você não pode entrar, é menor de idade.")

nome = input('Digite seu nome: ')

if nome == "":
    print("Por favor, digite um nome válido.")
elif nome == "Joao":
    print("Olha só, o dono da balada chegou.")
else:
    print("Olá "+ nome +"! Seja bem vindo a nossa balada.")

#MATCH CASE

match primeira_resposta: # Espera um String
    case 'a': # primera_resposta == 'a'? False
        print("Resposta incorreta.")
    case 'b':# primera_resposta == 'b'? True
        print("Resposta correta.")
    case 'c':
        print("Resposta incorreta.")
    case 'd':
        print("Resposta incorreta.")
    case 1:
        print("Resposta não pode ser númerica.")
    case _: # _ significa valor default, ou seja, valor padrão
        print("Resposta inválida.")


# VÁRIAS OPÇÕES EM UM CASE

dia = input('Digite o dia dessa semana: ')

match dia:
    case "sabado" | "domingo":
        print("Esse dia é em um FINAL DE SEMANA")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Esse dia é DURANTE A SEMANA")