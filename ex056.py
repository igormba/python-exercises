'''Desenvolva um programa que leia o nome, idade, sexo de 4 pessoas. No final do programa, mostre: - A média de idade do grupo, - Qual é nome do homem mais velho, - Quantas mulheres têm menos de 20 anos.'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {} PESSOAS -----'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média da idade do grupo é de {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))