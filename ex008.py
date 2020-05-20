#Escreva um programa que leia um valor em metros e o exiba convertidos em centimentos e milimetros.

print('Informe um número, que informaremos quantos centimentos e milimetros ele possui.')
metros = float(input('Informe um valor:'))
c = metros * 100
m = metros * 1000
print('{}m tem {:.0f}cm e {:.0f}mm.'.format(metros, c, m))

