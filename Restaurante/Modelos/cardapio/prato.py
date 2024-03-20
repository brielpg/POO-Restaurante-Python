from Restaurante.Modelos.cardapio.itemCardapio import ItemCardapio


class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f'Nome: {self._nome.ljust(13)} | Preço: R$ {self._preco} | Descriçao: ({self._descricao})'
