from abc import ABC, abstractmethod

class Transporte(ABC):

    def iniciar_processo(self):
        print("O calculo do frete está sendo iniciado... ")

    @abstractmethod
    def calcular_frete(self, distancia, peso):
        pass

class Caminhao(Transporte):
    def calcular_frete(self, distancia, peso):
        if peso <= 1000:
            print("Peso dentro do limite do caminhão")
            valor_frete = 5 * distancia
            print(f"O valor do frete foi: {valor_frete}")
        else:
            print("limite de peso excedido")

class Drone(Transporte):
    def calcular_frete(self, distancia, peso):
        if peso <= 2:
            print("Peso dentro do limite do drone ")
            valor_frete = 20 * distancia
            print(f"O valor do frete foi: {valor_frete}")
        else:
            print("Limite de peso excedido")


class Navio(Transporte):
    def calcular_frete(self, distancia, peso):
        if distancia >= 1000:
            print("Distancia minima aceita pelo navio")
            valor_frete = 10 * distancia
            print(f"O valor do frete foi: {valor_frete}")
        else:
            print("A distancia minima do navio é de 1000 km")


def processar_lote(lista_de_objetos):
    for transporte in lista_de_objetos:
        transporte.iniciar_processo()
        transporte.calcular_frete(1500, 1)

# 1. Tentativa de instanciar a Classe Abstrata (DEVE GERAR ERRO)
# Descomente a linha abaixo para testar e provar que o Python bloqueia:
# objeto_generico = Transporte()


# 2. Instanciando as Classes Filhas
transporte1 = Caminhao()
transporte2 = Drone()
transporte3 = Navio()

# 3. Criando um Lote de Processamento (Lista)
lote = [transporte1, transporte2, transporte3]


# 4. Processando em lote (Demonstrando o Polimorfismo e a Abstração)
print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
processar_lote(lote)






