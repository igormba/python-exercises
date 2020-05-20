'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120'''

from math import factorial
n = int(input('Informe um número: '))
c = n
print('Calculando {}! = '.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    c -= 1
print('{}'.format(factorial(n)))