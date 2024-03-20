from Restaurante.Modelos.restaurante import Restaurante
from Restaurante.Modelos.cardapio.bebida import Bebida
from Restaurante.Modelos.cardapio.prato import Prato
from Restaurante.Modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.avaliar_restaurante("Gui", 5)
restaurante_praca.avaliar_restaurante("Lais", 3.5)
restaurante_praca.avaliar_restaurante("Emy", 1)

bebida1 = Bebida('Suco de Manga', 5, '500ml')
prato1 = Prato('Lagosta', 65, 'A melhor lagosta do Brasil')
sobremesa1 = Sobremesa('Petit Gateau', 20, 'Quente/Fria', 'Médio')

bebida1.aplicar_desconto(5)

restaurante_praca.adicionar_ao_cardapio(bebida1)
restaurante_praca.adicionar_ao_cardapio(prato1)
restaurante_praca.adicionar_ao_cardapio(sobremesa1)


def main():
    Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio()


if __name__ == '__main__':
    main()
