import pandas as pd
df = pd.read_csv("funcionarios.csv", sep=";")
print(df)

print("Salários menores que que 3000: ")

print(df[df['salario'] < 3000])


