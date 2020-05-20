#Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere o dólar: US$1,00 = R$3,27.

real = float(input('Quando dinheiro você tem na carteira? R$'))
dolar = real / 5.49
euro = real / 6.09
print('Com R$ {:.2f}, você consegue comprar: \n US$ {:.2f} \n EUR {:.2f}'.format(real, dolar, euro))