'''Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção. No final, mostre a lista ordenada na tela.'''

num = list()
for n in range(0, 5):
    num.append(int(input('Informe um número: ')))
    num.sort()
print(f'Os números cadastrados na lista são {num}')