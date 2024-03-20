from Restaurante.Modelos.avaliacoes import Avaliacao
from Restaurante.Modelos.cardapio.itemCardapio import ItemCardapio


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliacao".ljust(25)} | Status')
        for i in cls.restaurantes:
            print(
                f'{i._nome.ljust(25)} | {i._categoria.ljust(25)} | {str(i.retornar_media_avaliacoes).ljust(25)} | {i.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'

    def alternar_estado(self):
        self._ativo = not self._ativo

    def avaliar_restaurante(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        if nota >= 1 and nota <= 5:
            self._avaliacoes.append(avaliacao)
        else:
            return 'Nota Inválida, tente valores entre 1 e 5!'

    @property
    def retornar_media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'

        soma_das_notas = sum(i._nota for i in self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_ao_cardapio(self, item):
        self._cardapio.append(item) if isinstance(item, ItemCardapio) else None

    def exibir_cardapio(self):
        print(f"Cardápio do Restaurante {self._nome}\n")
        for i, j in enumerate(self._cardapio, start=1):
            print(f"{i}. {j}")
