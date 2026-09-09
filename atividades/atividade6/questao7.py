orcamento = 500
print(f"seu saldo é de {orcamento}")
gastos = int(input("Digite o gasto realizado:"))
calculo = orcamento - gastos
sobra = 0
while gastos < orcamento:
    sobra = orcamento - gastos
    print("seu saldo é de", sobra)
    gastos += int(input("Digite o gasto realizado:"))
if sobra < orcamento:
    print("Atenção: Você ficou sem saldo ou estourou seu orçamento!")



