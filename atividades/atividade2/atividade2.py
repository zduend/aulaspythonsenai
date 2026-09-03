nome = input("Digite seu nome: " )
idade = int(input("Digite sua idade: " ))
plano = input("Você tem plano de saude? ") == "sim"
resultado = idade > 17 and idade < 65 and plano
print("Seu nome é:", nome, "Sua idade é:", idade,"anos","Tem plano de saúde?:", plano, "Voce foi aceito no plano?", resultado)