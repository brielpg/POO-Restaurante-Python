from Restaurante.Modelos.cardapio.itemCardapio import ItemCardapio


class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return f'Nome: {self._nome.ljust(13)} | Preço: R$ {self._preco} | Tamanho: ({self._tamanho})'
