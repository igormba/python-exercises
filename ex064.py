'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai para quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual é a soma entre eles (desconsiderando o flag)'''

n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Informe um número: '))
    if n != 999:
        cont += 1
        soma += n
print('Você informou {} números e a soma total deles é {}.'.format(cont, soma))
