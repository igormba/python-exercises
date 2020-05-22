'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.'''

produto = preco = maisdemil = maisbarato = total = 0
print('=-=' * 5)
print('MERCADO ANDRADE')
print('=-=' * 5)
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    total += preco
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if preco > 1000:
            maisdemil += 1
        if preco < 1000:
            maisbarato  = preco
            maisbarato = produto
    if continuar == 'N':
        break
print(f'O valor total da compra é R${total:.2f}.')
print(f'{maisdemil} produtos tem valor superior à R$1000.')
print(f'O produto mais barato é o {maisbarato}.')