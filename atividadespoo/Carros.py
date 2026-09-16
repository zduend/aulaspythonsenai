class Carros:
    def __init__(self, modelo, ano, portas, marchas, lugares):
        self.modelo = modelo
        self.ano = ano
        self.portas = portas
        self.marchas = marchas
        self.lugares = lugares

    def mostrarmodelocarros(self):
        print(self.modelo)

    def __str__(self):
        return f"Modelo do carro: {self.modelo}\nAno do carro: {self.ano}\nQuantas portas: {self.portas}\nMarchas: {self.marchas}\nlugares: {self.lugares}\n"

CarroGol = Carros("Gol", "1999", 2, 5, 5)
CarroCivic = Carros("Civic", "2001", 4, 6, 5)
CarroUno = Carros("Uno", "2013", 2, 5, 5)
CarroCorolla = Carros("Corolla", "2014", 2, 5, 5)
CarroOnix = Carros("Onix", "2015", 2, 5, 5)

todosOsCarros = [CarroCivic, CarroGol, CarroCorolla, CarroOnix, CarroUno]
for carro in todosOsCarros:
    print(carro)
