'''Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere o dólar: US$1,00 = R$5,49.'''

real = float(input('Quando dinheiro você tem na carteira? R$'))
dolar = real / 5.49
euro = real / 6.09
print(f'Com R$ {real:.2f}, você consegue comprar: \n US$ {dolar:.2f} \n EUR {euro:.2f}')