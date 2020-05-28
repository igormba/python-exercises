'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das Três listas geradas.'''

lista = list()
par = list()
impar = list()

while True:
    num = int(input('Informe um número: '))
    if num != 0:
        lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
print(f'{lista} foram todos os números digitados, inseridos na lista.')
print(f'{par} são os números PARES, inseridos na lista.')
print(f'{impar} são os números IMPARES, inseridos na lista.')