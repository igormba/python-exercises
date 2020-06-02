'''Crie um programa que leia o nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario
e todos os dicionarios em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) A media de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da media.'''

pessoas = dict()
nome = list()
sexo = list()
idade = list()
mulheres = list()

while True:
    nome.append(str(input('Nome: ')).strip().upper()[0])
    sx = ' '
    while sx not in 'MF':
        sx = str(input('Sexo: [M/F] ')).strip().upper()[0]
        sexo.append(sx)
    idade.append(int(input('Idade: ')))
    pessoas['Pessoas'] = nome[:]
    pessoas['Pessoas'] = sexo[:]
    pessoas['Pessoas'] = idade[:]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A) Ao todo {len(nome)} pessoas foram cadastradas.')
print(f'B) A média de idade é de {sum(idade) / len(idade):.2f}')



