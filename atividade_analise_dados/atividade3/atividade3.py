import pandas as pd
print(f"###################### FORMATAÇÃO DO CPF ######################")
df = pd.read_csv("dados_despadronizados.csv", dtype=str)
print(df.head())

df["cpf_formatado"] = (
    df["cpf"]
    .str.replace(".", "", regex=False)
    .str.replace("-","", regex=False)
    .str.replace(" ","", regex=False)
    )


print(df[["cpf_formatado"]].head())

df["cpf_valido"] = (
    (df["cpf_formatado"].str.len() == 11)
    &
    (df["cpf_formatado"].str.isdigit())
)

print(df[["cpf", "cpf_formatado","cpf_valido"]])
print()

print(f"###################### FORMATAÇÃO DO NÚMERO DE TELEFONE ######################")

df["numero_formatado"] = (
    df["numero"]
    .str.replace(r"\D","", regex=True)
)
print(df[["numero", "numero_formatado"]].head())
print()
tem_codigo_pais = (
    (df["numero_formatado"].str.startswith("55"))
    &
    (df["numero_formatado"].str.len() == 13)
)

df.loc[tem_codigo_pais, "numero_formatado"] = (
    df.loc[tem_codigo_pais, "numero_formatado"].str[2:]
)

print(df[["numero", "numero_formatado"]].head(6))
print()

df["numero_valido"] = (
    (df["numero_formatado"].str.len() == 11)
    &
    (df["numero_formatado"]).str.isdigit()
)

print(df[["numero", "numero_formatado", "numero_valido"]])
print()

print(f"###################### FORMATAÇÃO DOS SALÁRIOS ######################")

tem_virgula = df["salario"].str.contains(",", regex=False)
print(df.loc[tem_virgula,["salario"]])

df["salario_formatado"] = df["salario"].copy()

df.loc[tem_virgula,"salario_formatado"] = (
    df.loc[tem_virgula,"salario_formatado"]
    .str.replace(".", "", regex=False)
)

df["salario_formatado"] = (
    df["salario_formatado"]
    .str.replace(",",".", regex=False)
    .str.replace("R$","",regex=False)
    .str.strip()
)


df["salario_formatado"] = df["salario_formatado"].astype(float)



df = df[[
    "nome",
    "cpf",
    "cpf_formatado",
    "cpf_valido",
    "numero",
    "numero_formatado",
    "numero_valido",
    "salario",
    "salario_formatado",
]]
print(df.head())

df.to_csv("dados_padronizados.csv", index=False)

print("Arquivo salvo com sucesso!")

df_verificacao = pd.read_csv("dados_padronizados.csv", dtype=str)

print(df_verificacao.shape)
print(df_verificacao.columns)
print(df_verificacao.loc[16, ["nome", "salario", "salario_formatado"]])




