
#Questão 01

#A maneira que o aluno escreveu o código não está correta porque ele esta dando o print antes de definir a variavel nome 
#A forma correta é:
nome = input("Digite seu nome")
print("Bem vindo(a),", nome )

#Questão 03

#O resultado está dando 1010, porque a variavel n1 e n2 deveriam está usando a função "int"
#o python uniu os textos ao invés de somar, por que na verdade ele está concatenando as duas variaveis.
#forma correta:
n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
resultado = n1 + n2
print("O resultado da soma é: ", resultado) 

#Questão 04
#O resultado impresso na tela será:
valor de A: 4
valor de B: 9
#Justificativa:
A = 8 #Atribuido o valor de 8 a variável A
B = 4 #Atribuido o valor de 4 a variavel B
A = B #Ver o que tem dentro de B e coloca na variávl A,(A = 4, B = 4)
B = A + 5 #Aqui soma A = 4, com +5 (4+5=9) 
print("Valor de A:", A) #mostra o valor que está dentro de A
print("Valor de B:", B) #mostra o valor atual de B

