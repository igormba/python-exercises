'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

lista = list()
pessoas = dict()
idade = 0

while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: ').strip().title())
    pessoas['Sexo'] = ' '
    while pessoas['Sexo'] not in 'MF':
        pessoas['Sexo'] = str(input('Sexo: ').strip().upper())
    pessoas['Idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    idade += pessoas['Idade']
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if continuar == 'N':
        break
print(f'A) Ao todo, {len(lista)} pessoas foram cadastradas.')
print(f'B) A média de idade do grupo é {idade / len(lista):.2f} anos.')
print(f'C) As Mulheres cadastradas: ', end='')
for c in lista:
    if c['Sexo'] == 'F':
        print(f'{c["Nome"]}', end=' ')
print(f'\nD) Pessoas com idade acima da média: ', end=' ')
for c in lista:
    if c['Idade'] >= (idade/len(lista)):
        print(f'{c["Nome"]} com {c["Idade"]} anos.')



