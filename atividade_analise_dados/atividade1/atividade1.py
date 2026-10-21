import pandas as pd

df = pd.read_csv("funcionarios.csv", sep=";")

#IMPRIMINDO SALÁRIOS MENORES QUE 300
print("Estes são os salários menores que que 3000: ")
print(df[df['salario'] < 3000])
print()
#IMPRIMINDO CARGOS SELECIONADOS
cargos = [
    "Analista de Dados",
    "Analista de Sistemas",
    "Desenvolvedor Java",
    "Cientista de Dados"
]
print("Funionarios com cargos de:\n "
      "- Analista de Dados\n "
      "- Analista de Sistemas\n "
      "- Desenvolvedor Java\n "
      "- Cientista de Dados\n ")

print(df[df["cargo"].isin(cargos)]["nome"])
print()

#LISTAR OS NOMES E OS CARGOS DE QUEM TEM O SALÁRIO MAIOR QUE 6000

print("Nomes e cargos de quem tem o salário maior que 6000:")
print(df[df["salario"] > 6000][["nome","cargo"]])
print()

#LISTAR FUNCIONARIOS COM O ID PAR
print(df[df["id"] % 2 == 0])