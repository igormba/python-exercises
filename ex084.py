'''Faça um programa qye leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

lista = list()
pessoas = list()
peso = list()
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    pessoas.append(lista[:])
    peso.append(lista[1])
    lista.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'O maior peso digitado é {max(peso)}Kg, que pertence a', end=' ')
for p in pessoas:
    if p[1] == max(peso):
        print(f'{p[0]}.')
print(f'O menor peso digitado é {min(peso)}Kg, que pertence a', end=' ')
for p in pessoas:
    if p[1] == min(peso):
        print(f'{p[0]}.', end='')
