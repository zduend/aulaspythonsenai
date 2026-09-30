valordacompra = float(input("Digite o valor da compra: "))
vip = int(input("Você é VIP? digite 1 para sim ou 0 para não"))
valorfretegratis = 200.00
validarvip = 1
resultado = valordacompra >= valorfretegratis and vip == validarvip
print("Tem direito a frete grátis?", resultado)

