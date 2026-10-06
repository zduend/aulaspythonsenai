# FORMA DOS DADOS EM LISTAS E TUPLAS -> USAM INDEX
#       index     0        1        2
lista_nomes = ['João', 'Bianca', 'Italo']
tupla_nomes = ('João', 'Bianca', 'Italo')

# FORMA DOS DADOS EM DICIONÁRIO -> USAM CHAVES E VALORES
  # chave  :  valor
dicionario_nomes = {
    "nome1": "Maria",
    "nome2": "Jose",
    "nome3": "Bruno",
}

dicionario_ing_por = {
    'hi': 'Olá',
    'bye': 'Tchau'
}
pesquisa = input('Digite a palavra que quer traduzir:\nInglês: ')

if pesquisa in dicionario_ing_por:
    print(f'Português: {dicionario_ing_por[pesquisa]}')
else:
    print("Palavra não encontrada")

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def identidade(self):
        print(f'Nome do Pessoa: {self.nome}\n'
              f'Idade: {self.idade}\n'
              f'Cpf: {self.cpf}')

pessoa1 = {
    'nome': 'João',
    'idade': 22,
    'cpf': '111.222.333-44',
}

obj_pessoa = Pessoa(pessoa1['nome'],
                    pessoa1['idade'],
                    pessoa1['cpf'])

obj_pessoa.identidade()#JSON = JavaScript Object Nomenclature

alunos = [
    {
        'nome': 'Fulano',
        'idade': 22,
        'cpf': '111.222.333-44',
        'materias': ['matematica', 'ciências', 'português']
    },
    {
        'nome': 'Ciclano',
        'idade': 33,
        'cpf': '111.222.333-55',
        'materias': ['Python', 'Java', 'SQL']
    }
]

# chaves = nome, idade
dicionario_pessoa = {
    'nome': 'fulano',
    'idade': 22,
}

print(dicionario_pessoa)
dicionario_pessoa['Cidade'] = 'Brasília'# adicionando valor novo no dicionario

print(dicionario_pessoa.get('nome')) # metodo get
print(dicionario_pessoa['idade'])    # buscando pela chave
print(dicionario_pessoa.get('cpf'))  # metodo get

dicionario_pessoa.pop('idade')
print(dicionario_pessoa)
adicionar_chave = input("Digite um valor para adicionar: ")
adicionar_valor = input("Digite um valor para adicionar: ")
dicionario_pessoa[adicionar_chave] = adicionar_valor
print(dicionario_pessoa)
dicionario_pessoa['CEP'] = None
print(dicionario_pessoa)

dicionario_venda = {
    'nome': 'Frango',
    'Preço': 25.00
}

#printa na tela os nomes das chaves
for venda in dicionario_venda:
    print(venda)

#printa na tela os valores
for venda in dicionario_venda.values():
    print(venda)

for nome, preco in dicionario_venda.items():
    print(f'Chave: {nome}\n'
          f'Valor: {preco}\n')