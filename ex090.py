'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

dicionario = dict()
dicionario['Nome'] = str(input('Nome: '))
dicionario['Média'] = float(input(f'Média de {dicionario["Nome"]}: '))
print('-=' * 20)
print(f'Nome é igual a {dicionario["Nome"]}')
print(f'Média é igual a {dicionario["Média"]}')
if dicionario['Média'] >= 7:
    print('Situação do aluno é APROVADO!')
    dicionario['Situação'] = 'Aprovado'
elif dicionario['Média'] >= 6.1:
    print('Situação do aluno é em RECUPERAÇÃO!')
    dicionario['Situação'] = 'Recuperação'
if dicionario['Média'] <= 6:
    print('Situação do aluno é REPROVADO!')
    dicionario['Situação'] = 'Reprovado'
print(dicionario)