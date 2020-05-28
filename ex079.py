'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = list()
while True:
    num = int(input('Informe um número: '))
    if num not in lista:
        lista.append(num)
    else:
        print('Número já incluso')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if num not in lista:
            lista.append(num)
    if continuar == 'N':
        break
lista.sort()
print(f'Os números digitados foram {lista}')