from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida("suco de melancia",5.00, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho',2.00,'O melhor pãozinho da cidade')
prato_paozinho.aplicar_desconto()
sorvete_morango = Sobremesa('sorvete de morango',7.00,'morango','médio','Delicioso sorvete artesanal de morango')
sorvete_morango.aplicar_desconto()
restaurante_praca.adicionar_item_ao_cardapio(bebida_suco)
restaurante_praca.adicionar_item_ao_cardapio(prato_paozinho)
restaurante_praca.adicionar_item_ao_cardapio(sorvete_morango)
print('\n')

def main():
   restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
