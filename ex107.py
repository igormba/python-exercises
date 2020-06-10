'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from modulos import moeda

preco = float(input('Informe o preço: R$ '))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentando o preço em 10%, temos R${moeda.aumentar(preco, 10)}')
print(f'Diminuindo o preço em 20%, temos RS{moeda.diminuir(preco, 20)}')