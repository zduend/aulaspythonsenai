class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque


    def adicionar_estoque(self, quantidade):
            if quantidade > 0:
                self.__quantidade_estoque += quantidade
            else:
                print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade):
        if quantidade > 0 and quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
        else:
            print("Venda negada: Estoque insuficiente")


    def aplicar_desconto(self, percentual):
        if percentual > 0 and percentual <= 80:
           desconto = self.__preco * percentual / 100
           self.__preco -= desconto
        else:
            print("Erro: Desconto inválido")


    def exibir_resumo(self):
        print(f"Nome do produto: {self.__nome}")
        print(f"Preco do produto: {self.__preco}")
        print(f"Quantidade de estoque: {self.__quantidade_estoque}")

placa_de_video = Produto("GTX 4060", 3500, 100)
placa_de_video.__quantidade_estoque = -50
placa_de_video.__preco = -100
placa_de_video.realizar_venda (9999)

placa_de_video.exibir_resumo()

print(placa_de_video.__dict__)




