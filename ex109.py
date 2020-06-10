'''Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from modulos import moeda

preco = float(input('Informe o preço: R$ '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando o preço em 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo o preço em 20%, temos {moeda.diminuir(preco, 20, True)}')