'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade.
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar.
Se já passou do tempo de alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
print('-=-' * 8)
print('FORÇAS ARMADAS DO BRASIL')
print('-=-' * 8)
nome = str(input('Qual o seu nome? ')).strip()
idade = int(input('Em que ano você nasceu? '))
anoatual = date.today().year
anoeidade = date.today().year - idade
if (anoatual - idade) <= 17:
    print('Você nasceu no ano de {} e tem {} anos.'.format(idade, anoeidade))
    print('Não está na hora de realizar o alistamento militar.', end=' ')
    falta = anoatual - idade
    falta1 = 18 - falta
    print('Retorne para o alistamento em {} anos.'.format(falta1))
elif (anoatual - idade) == 18:
    print('Você nasceu no ano de {} e completa {} anos em {}.'.format(idade, anoeidade, anoatual))
    print('FAÇA AGORA O ALISTAMENTO MILITAR!')
elif (anoatual - idade) >= 19:
    print('Você nasceu no ano de {} e tem {} anos.'.format(idade, anoeidade))
    excedeu = (anoatual - idade) - 18
    print('Já passou da hora de realizar o alistamento militar.', end=' ')
    print('Você deveria ter feito o alistamento militar a {} anos.'.format(excedeu))
print('Boa sorte!')



