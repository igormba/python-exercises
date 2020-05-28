'''Crie um programa que vai ler vários números e coloque-os em uma lista. Depois disso, mostre: 
A) Quantos números foram digitados.
B) A lista de valores ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = list()
while True:
    lista.append(int(input('Informe um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'Os valores digitados foram {lista}.')
print(f'{len(lista)} números foram inseridos na lista.')
if 5 in lista:
    print(f'O número 5 está incluso na lista, na posição {lista.index(5)}.')
else:
    print('O número 5 não foi inserido na lista.')