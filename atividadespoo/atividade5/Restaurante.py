class ItemPedido:
    def __init__(self, descricao: str, valor: float):
        self.descricao = descricao
        self.valor = valor

class Mesa:
    def __init__(self,numero_mesa: int, pedidos):
        self.numero_mesa = numero_mesa
        self.pedidos = pedidos[""]

    def adicionar_pedido(self, item):
        self.pedidos.append(item)
        print(f"{item.descricao} adicionado a {self.numero_mesa}.")











