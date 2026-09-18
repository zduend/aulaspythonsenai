class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    @property
    def nome(self):
        return self.__nome

    def preco(self, novo_preco):
        if novo_preco < 0:
            print("Não é possivel colocar produtos com valores negativos")
        else:
            self.__preco = novo_preco

    def adicionar_estoque(self, novo_quantidade):
        if novo_quantidade > 0:
            self.__quantidade_estoque += novo_quantidade
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self):





