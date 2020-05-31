'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da
casa, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado.'''

print('-=-' * 12)
print('Seja vem vindo ao Banco Andrade')
print('-=-' * 12)
print(' ')
print('Meu nome é Igor e eu sou o gerente que irá te atender.')
print(' ')
nome = str(input('Qual seu nome? '))
casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual é o salário: R$'))
prazo = int(input('Quantos anos para parcelamento: '))
parcelamento1 = casa / (prazo * 12)
parcelamento2 = salario * 30 / 100
if parcelamento2 >= parcelamento1:
    print(f'Seu emprestimo foi aprovado, com parcelas mensais de R${parcelamento1:.2f}!')
else:
    print('Infelizmente seu emprestimo não foi aprovado.')
print(' ')
print('O Banco Andrade te deseja um ótimo dia!')

