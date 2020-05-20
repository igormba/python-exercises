# Faça um programa que leia o ano qualquer e informe se ele é BISSEXTO.

from datetime import date
ano = int(input('Informe o ano a ser analisado? Digite 0 para consulta do ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!')