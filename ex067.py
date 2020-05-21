'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número digitado for negativo.'''

while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 12)
    if n < 0:
        break
    for tabu in range(1, 11):
        print(f'{n} x {tabu:2} = {n*tabu}')
    print('-' * 12)
print('Tabuada Finalizada!')


