class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def __str__(self):
        return f'nome: {self.nome}, idade: {self.idade}, raça: {self.raca}'

cachorro1 = Cachorro("Rex", 5, "Buldog")
cachorro2 = Cachorro("Zeus", 4, "PastorAlemao")

cachorro3 = Cachorro("Bolinha", 1, "Doberman")

lista = [cachorro1, cachorro2]

with open("lista_de_cachorros.txt", 'w', encoding='utf-8') as arquivo:
    for cachorro in lista:
        arquivo.write(f"Cachorro: {str(cachorro)}\n")

with open("lista_de_cachorros.txt", 'a', encoding='utf-8') as arquivo:
    arquivo.write(f"Cachorro: {str(cachorro3)}")

with open("lista_de_cachorros.txt", 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    posicao = texto.find("Rex")
    #                         60 -> 64
    cachorro_zeus = texto[posicao:posicao+3]

    cachorro_rex = texto[16:19]

print(cachorro_zeus)

with open("C:\\teste\\EXEMPLO TXT\\nomes.txt", 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    nome_arquivo = texto[2:2+4]

class Exemplo:
    def __init__(self, nome):
        self.__nome = nome

    @property #get
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


obj = Exemplo(nome_arquivo)
print(f"Nome achado no arquivo nomes.txt: {obj.nome}")#get