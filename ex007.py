'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''

print('Apresentação de média escolar.')
nome = input('Informe seu nome: ')
m1 = float(input('Informe a primeira nota: '))
m2 = float(input('Informe a segunda nota: '))
s = (m1 + m2) / 2
print(f'{nome} a sua média é {s:.1f}!')