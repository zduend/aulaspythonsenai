import pandas as pd

base_de_dados = "../atividade1/funcionarios.csv"
df = pd.read_csv(base_de_dados, sep=";")
print(df.columns.tolist())

#filtrando dados com salaraios acima de 6k
salarios_altos = df[
    (df["salario"] > 6000)
]
print(salarios_altos)

#transformo tabela filtrada em df
salarios_altos = pd.DataFrame(salarios_altos)

salarios_altos.to_csv("salarios_altos.csv", index=False, sep=";")
df_filtrado = pd.read_csv("salarios_altos.csv", sep=";")
print(df_filtrado)

novo_funcionario = [{
    "id": 100,
    "nome": "Joao de menezes",
    "salario": 15000,
    "cargo": "Instrutor",
},
    {
        
    }]

df_novo_funcionario = pd.DataFrame(novo_funcionario)
df_filtrado =  pd.concat([df_filtrado, df_novo_funcionario], ignore_index=True)
print(df_filtrado)
