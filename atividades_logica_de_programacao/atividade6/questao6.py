numero_secreto = 12
descubra = int(input("Descubra o numero secreto"))
tentativa = 1
print(f"Você errou. Tentativa {tentativa}")
while descubra != numero_secreto:
    tentativa += 1
    descubra = int(input("descubra o numero secreto"))
    print(f"Tentativa {tentativa}")
print(f"Parabéns! Você acertou o número secreto em {tentativa} tentativas!")


