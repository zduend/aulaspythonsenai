import pandas as pd

# Carregamento dos dados
df = pd.read_csv("estoque_supermercado.csv")

# Limpeza coluna preco
df["preco"] = df["preco"].str.replace("R$", "")
df["preco"] = df["preco"].str.strip()
df["preco"] = df["preco"].str.replace(",", ".")

# Conversão valores numéricos
df["preco"] = pd.to_numeric(df["preco"], errors="coerce")

# Substituição de NaN pela média
media_preco = df["preco"].mean()
df["preco"] = df["preco"].fillna(media_preco)


# Limpeza coluna quantidade
df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
df["quantidade"] = df["quantidade"].fillna(0)
df["quantidade"] = df["quantidade"].astype(int)

# Limpeza da coluna setor
df["setor"] = df["setor"].str.strip()
df["setor"] = df["setor"].str.lower()
df["setor"] = df["setor"].fillna("sem setor")

# Tratamento das datas
df["data_compra"] = pd.to_datetime(
    df["data_compra"], format="%d/%m/%Y", errors="coerce"
)

df["data_vencimento"] = pd.to_datetime(
    df["data_vencimento"], format="%d/%m/%Y", errors="coerce"
)

print("\n--- BASE DE DADOS LIMPA ---")
print(df.head(10))
print(df.dtypes)

# Período de análise
data_inicio = pd.to_datetime("27/10/2026", format="%d/%m/%Y")
data_fim = pd.to_datetime("03/11/2026", format="%d/%m/%Y")

# Filtrando os produtos
produtos_vencendo = df[
    (df["data_vencimento"] >= data_inicio) &
    (df["data_vencimento"] <= data_fim)
]

print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
print(produtos_vencendo)

print("\n--- MAIOR QUANTIDADE A VENCER ---")

if not produtos_vencendo.empty:
    indice_maior = produtos_vencendo["quantidade"].idxmax()
    produto_maior = produtos_vencendo.loc[indice_maior]

    print(produto_maior[["nome", "quantidade", "data_vencimento"]])
else:
    print("Nenhum produto vencendo nesta semana.")


data_compra_inicio = pd.to_datetime("24/10/2026", format="%d/%m/%Y")

compras_recentes = df[
    (df["data_compra"] >= data_compra_inicio) &
    (df["data_compra"] <= data_inicio)
]

print("\n--- COMPRAS RECENTES ---")
print(compras_recentes)

produtos_sem_vencimento = df[df["data_vencimento"].isna()]

print("\n--- PRODUTOS SEM VENCIMENTO ---")
print(produtos_sem_vencimento)

# Calculando o valor total de cada produto
df["valor_total_estoque"] = df["preco"] * df["quantidade"]

# Somando o valor do estoque por setor
valor_por_setor = df.groupby("setor")["valor_total_estoque"].sum()

print("\n--- VALOR PATRIMONIAL POR SETOR ---")
print(valor_por_setor)

print("\n--- MAIOR VALOR PATRIMONIAL POR SETOR ---")
print(valor_por_setor.idxmax())
print(valor_por_setor.max())