class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def aplicar_desconto(self, desconto):
        self._preco -= (self._preco * (desconto/100))
