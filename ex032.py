'''Faça um programa que leia o ano qualquer e informe se ele é BISSEXTO.'''

from datetime import date
ano = int(input('Qual ano deseja analisar? Digite 0 para consulta do ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO!')