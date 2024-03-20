from Restaurante.Modelos.cardapio.itemCardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho

    def __str__(self):
        return f'Nome: {self._nome.ljust(13)} | Preço: R$ {self._preco} | Tipo: {self._tipo} | Tamanho: {self._tamanho}'
