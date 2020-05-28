'''Escreva um programa que leia um valor em metros e o exiba convertidos em centimentos e milimetros.'''

print('Informe um número, que informaremos quantos centimentos e milimetros ele possui.')
metros = float(input('Informe um valor: '))
c = metros * 100
m = metros * 1000
print(f'{metros}m tem {c:.0f}cm e {m:.0f}mm.')

