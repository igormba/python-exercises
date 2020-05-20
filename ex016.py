'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex: Digite número: 6.127. O número 6.127 tem a parte inteira 6.'''

from math import trunc
valor = float(input('Digite um número: '))
print('Você digitou {} e a sua porçao inteira é {}'.format(valor, trunc(valor)))