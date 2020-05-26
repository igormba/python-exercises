'''Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

lista = ('Lápis', 1.80, 'Borracha', 2.30, 'Caderno', 18.90, 'Estojo', 39, 'Compasso', 9.90, 'Mochila', 300, 'Canetas', 9.99, 'Livros', 99.99)

print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-' * 40)


