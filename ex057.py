'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitação
novamente até ter um valor correto.'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input("Digite o seu sexo: [M/F] ")).strip().upper()[0]
    if sexo == 'M' or sexo == 'F':
        print('O Sexo informado foi {}.'.format(sexo))
    else:
        print('Opção incorreta. Favor digitar M ou F.')


