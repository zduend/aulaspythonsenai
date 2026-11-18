import pandas as pd
import numpy as np

# Carregamento dos dados
df = pd.read_csv("vendas_mercados.csv", sep="\t")

# Verificando a base
print(df.head())
print(df.dtypes)

# QUESTÃO 1
df["Lucro"] = (
    df["Preco_Unitario"] - df["Custo_Unitario"]
) * df["Quantidade"]
lucro_por_mercado = df.groupby("Mercado")["Lucro"].sum()
print("\n--- LUCRO POR MERCADO ---")
print(lucro_por_mercado)
print("\n--- MERCADO COM MAIOR LUCRO ---")
print(lucro_por_mercado.idxmax())
print(f"R$ {lucro_por_mercado.max():.2f}")

# QUESTÃO 2

pagamentos = df.groupby(
    ["Regiao", "Forma_Pagamento"]
).size()

print("\n--- FORMAS DE PAGAMENTO POR REGIÃO ---")
print(pagamentos)

# Identificando a forma de pagamento mais utilizada
pagamento_mais_usado = pagamentos.groupby(level=0).idxmax()

print("\n--- PAGAMENTO MAIS UTILIZADO POR REGIÃO ---")
print(pagamento_mais_usado)