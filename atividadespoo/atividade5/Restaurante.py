class ItemPedido:
    def __init__(self, descricao: str, valor: float):
        self.descricao = descricao

        try:
            self.valor = float(valor)
        except ValueError:
            raise ValueError (f"Erro: O valor para '{descricao}' deve ser estritamente numérico. ")

class Mesa:
    def __init__(self,numero_mesa):
        self.numero_mesa = numero_mesa
        self.lista_pedidos = []

    def adicionar_pedido(self, item):
        self.lista_pedidos.append(item)
        print(f"-> {item.descricao} adicionado à {self.numero_mesa}" )

    def somar_total(self):
        total = 0
        for pedido in self.lista_pedidos:
            total += pedido.valor
        return total

    def fechar_conta(self,taxa_servico):
        subtotal = self.somar_total()
        valor_taxa = subtotal * taxa_servico / 100
        total_final = subtotal + valor_taxa
        for pedido in self.lista_pedidos:
            print(f"Pedido:{pedido.descricao} Valor:{pedido.valor:.2f}")

        print(f"Subtotal: {subtotal:.2f}")
        print(f"Valor taxa de serviço: {valor_taxa:.2f}")
        print(f"Total: {total_final:.2f}")

        self.lista_pedidos.clear()

# Função auxiliar para simular a interface do sistema e capturar as exceções sem quebrar
def registrar_pedido_seguro(mesa, descricao, valor):
    try:
        item = ItemPedido(descricao, valor)
        mesa.adicionar_pedido(item)
    except ValueError as erro:
        print(f"ALERTA DO SISTEMA: {erro}")

# 1. Instanciando as mesas
mesa1 = Mesa("mesa 1")

# 2. Registrando pedidos válidos
registrar_pedido_seguro(mesa1, "Pizza Margherita", 45.90)
registrar_pedido_seguro(mesa1, "Refrigerante", 8.50)

# 3. Testando o Tratamento de Exceções (Simulando erro de digitação do garçom)
print("\n--- TESTANDO ENTRADA INVÁLIDA ---")
registrar_pedido_seguro(mesa1, "Pudim", "quinze")  # Deve exibir o ALERTA DO SISTEMA e não quebrar
registrar_pedido_seguro(mesa1, "Café", "5,50")     # Erro comum de vírgula, deve acionar o ALERTA

# 4. Adicionando mais um pedido válido após o erro
registrar_pedido_seguro(mesa1, "Suco de Laranja", 12.00)

# 5. Fechando a conta com 10% de taxa de serviço
print("\n--- FECHAMENTO DA CONTA ---")
mesa1.fechar_conta(taxa_servico=10)

# 6. Verificando se a mesa foi limpa
print("\n--- VERIFICANDO STATUS DA MESA APÓS FECHAMENTO ---")
mesa1.fechar_conta(taxa_servico=10) # A conta deve vir zerada


















