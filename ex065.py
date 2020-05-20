'''Crie um progrma que leia vários números inteiros pelo teclado. No final da execusão, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.'''

r = 'S'
soma = quant = media = maior = menor = 0
while r in 'S':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input('Quer continuar? [S/N]')).strip().upper()
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media), end=' ')
print('O maior valor digitado foi {} e o menor valor foi {}.'.format(maior, menor))