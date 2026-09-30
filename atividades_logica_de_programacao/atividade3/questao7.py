'''
RESPOSTA:
O input para digitar a senha naturalmente se ler como str, sendo necessário a função int.
'''

senha_cadastrada = 1234
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)





