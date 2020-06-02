'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, o ano em que a pessoa vai se aposentar.'''

from datetime import date

anoatual = date.today().year
idade = aposentadoria = 0
dicionario = dict()

dicionario['Nome'] = str(input('Nome: '))
dicionario['Ano de Nascimento'] = int(input('Ano de Nascimento: '))
dicionario['CTPS'] = int(input('Nº CTPS (0 não tem): '))
idade = anoatual - dicionario['Ano de Nascimento']
dicionario['Idade'] = idade

if dicionario['CTPS'] != 0:
    dicionario['Ano de Contratação'] = int(input('Ano de Contratação: '))
    dicionario['Salário'] = float(input('Salário: R$ '))
    aposentadoria = dicionario['Ano de Contratação'] + 35

else:
    print('-=' * 30)
    print(f'Nome: {dicionario["Nome"]}\nIdade: {dicionario["Idade"]}\nNº CTPS: {dicionario["CTPS"]}')

print('-=' * 30)
print(f'Nome: {dicionario["Nome"]}\nIdade: {dicionario["Idade"]}\nNº CTPS: {dicionario["CTPS"]}\n'
      f'Ano de Contratação: {dicionario["Ano de Contratação"]}\nSalário: R$ {dicionario["Salário"]}\n'
      f'Aposentadoria: {aposentadoria}')
