from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida("suco de melancia",5.00, 'grande')
prato_paozinho = Prato('Pãozinho',2.00,'O melhor pãozinho da cidade')

restaurante_praca.adicionar_item_ao_cardapio(bebida_suco)
restaurante_praca.adicionar_item_ao_cardapio(prato_paozinho)

def main():
   restaurante_praca.exibir_cardapio
   
if __name__ == '__main__':
    main()
