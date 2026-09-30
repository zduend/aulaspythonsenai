'''
Construa um sistema escolar que leia a Nota 1 e a Nota 2 de um aluno, além da sua Porcentagem de Frequência. O programa deve primeiro calcular a média das notas. Para o aluno ser aprovado, ele precisa de duas coisas ao mesmo tempo: uma média maior ou igual a 6.0 E uma frequência maior ou igual a 75. Exiba a média calculada e, em seguida, exiba True se ele foi aprovado ou False se reprovou, usando o operador and.

'''

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
frequencia = int(input("Digite sua frequencia: "))
media = (nota1 + nota2) / 2
regraaprov = (media >= 6.0) and ( frequencia >= 75)
print("Sua média foi: ", media)
print("Você foi aprovado?: ", regraaprov)



