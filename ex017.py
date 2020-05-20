'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
e mostre o comprimento da hipotenusa.'''

from math import hypot
CO = float(input('Comprimento do Cateto Oposto: '))
CA = float(input('Comprimento do Cateto Adjacente: '))
HI = hypot(CO, CA)
print('A Hipotenusa vai medir {:.2f}'.format(HI))



'''co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''
