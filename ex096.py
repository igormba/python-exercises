'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def linha():
    print('=' * 30)

def area():
    resultado = l * c
    print('=' * 50)
    print(f'A área total do terreno {l}X{c}é {resultado} metros.')

linha()
print('     CONTROLE DE TERRENOS')
linha()
l = float(input('Largura (M): '))
c = float(input('Comprimento (M): '))
area()


