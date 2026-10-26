import pandas as pd


#Leia os dados do arquivo funcionarios.csv e crie um novo arquivo chamado cargos_altos.csv,
# contendo apenas os funcionários com salário acima de 6000.

print(f"Lendo os dados do arquivo funcionarios.csv, criando\nnovo arquivo cargos_altos.csv com os salários filtrados: ")
df = pd.read_csv("../atividade1/funcionarios.csv", sep=";")
funcionarios_altos = df[df["salario"] > 6000]
print(funcionarios_altos)
funcionarios_altos.to_csv("cargos_altos.csv", index=False, sep=";")

print()

#Cadastre mais funcionários, cada um com id, nome, salario e cargo, utilizando cargos diferentes
# dos já existentes.

print("Cadastrando novos funcionários na base de dados: ")
df.loc[len(df)] = [31, "Pedro Henrique", 4500.0, "Arquiteto de Software"]
df.loc[len(df)] = [32, "Samuel da Silva", 16000.0, "Especialista em IA"]
print(df.tail())

print()

#Remova os dois primeiros funcionários do arquivo, considerando os índices (index) 0 e 1.

print("Removendo Funcionarios index 0 e 1 da base de dados: ")
df = df.drop(index=[0,1])
print(df.head())

print()

#Crie uma nova coluna chamada tempo_empresa, que armazenará o tempo de permanência de cada funcionário
# na empresa em meses, utilizando valores do tipo inteiro (int).

print(f"Criando nova coluna tempo_empresa armazenando tempo de\npermanancia de cada funcionário na empresa em meses: ")

df["tempo_empresa"] = 12
df.loc[2, "tempo_empresa"] = 46
print(df.head())
print()

#Adicione um novo funcionário com o cargo de Estagiário, registrando seu tempo de empresa como int.

print(f"Adicionando novo funcionário com cargo de estagiário, com o registro de\ntempo de empresa: ")
df.loc[df.index.max() + 1] = [33, "Erick de Sá", 1500.0, "Estagiário", 6]
print(df.tail())
print()

#Confira se as alterações foram aplicadas corretamente e se os arquivos CSV estão salvos com os dados atualizados.
print("Salvando novos funcionarios no arquivo csv: ")
df.to_csv("funcionarios_atualizados.csv", index=False, sep=";")
df_verificacao = pd.read_csv("funcionarios_atualizados.csv", sep=";")
print(df_verificacao.tail())

print(df_verificacao["tempo_empresa"].dtype)












