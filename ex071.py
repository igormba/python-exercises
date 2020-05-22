'''Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor será entregue.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=-=' * 5)
print('BANCO ANDRADE')
print('=-=' * 5)
lista = [100, 50, 20, 10, 5, 2]
valor = int(input('Insira o valor que desaja sacar R$ '))
cont = 0
while True:
    if valor >= lista[cont]:
        nota = valor // lista[cont]
        print(f'Total de {nota} notas de R$ {lista[cont]}')
        valor = valor % lista[cont]
    cont += 1
    if valor == 0:
        break
print('Volte sempre ao Banco Andrade! Tenha um bom dia!')