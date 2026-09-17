class Carros:
    def __init__(self, modelo, ano, portas, marchas, lugares):        #CONSTRUTOR
        self.modelo = modelo
        self.ano = ano
        self.portas = portas          #ATRIBUTOS
        self.marchas = marchas
        self.lugares = lugares


    def __str__(self):
        return f"\tModelo do carro: {self.modelo}\n\tAno do carro: {self.ano}\n\tQuantas portas: {self.portas}\n\tMarchas: {self.marchas}\n\tlugares: {self.lugares}\n\t"

    def mostrarmodelocarros(self):
        print(self.modelo)

    def ligar(self):
        print(f"O {self.modelo} foi ligado!")                       # METODOS CONVÊNCIONAIS

    def desligar(self):
        print(f"O {self.modelo} está ligando...")

      

Carro1 = Carros("Parati", 1999, 2, 5, 5)
Carro2 = Carros("Marea", 2001, 4, 6, 5)
Carro3 = Carros("Uno", 2013, 2, 5, 5)                     #OBJETOS E INSTÂNCIAS
Carro4 = Carros("Corolla", 2014, 2, 6, 5)
Carro5 = Carros("Golf", 2000, 2, 5, 5)

todosOsCarros = [Carro1, Carro2, Carro3, Carro4, Carro5]

for carro in todosOsCarros:
    print(carro)
    carro.desligar()
    carro.ligar()
    print()

