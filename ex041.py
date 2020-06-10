'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUNIOR
Até 20 anos: SENIOR
Acima: MASTER'''

from datetime import date
print('-=-' * 16)
print('Seja bem-vindo a Confederação Nacional de Natação')
print('-=-' * 16)
ano = date.today().year
nome = str(input('Qual seu nome? ')).strip()
nascimento = int(input('Informe o ano do seu nascimento: '))
idade = ano - nascimento
if idade <= 9:
    print('Olá {}, como você tem {} anos, vai fazer parte da categoria MIRIM.'.format(nome, idade))
elif idade <= 14:
    print('Olá {}, como você tem {} anos, vai fazer parte da categoria INFANTIL.'.format(nome, idade))
elif idade <= 19:
    print('Olá {}, como você tem {} anos, vai fazer parte da categoria JUNIOR.'.format(nome, idade))
elif idade == 20:
    print('Olá {}, como você tem {} anos, vai fazer parte da categoria SENIOR.'.format(nome, idade))
else:
    print('Olá {}, como você tem {} anos, vai fazer parte da categoria MASTER.'.format(nome, idade))
print('Boa sorte e tenha um bom dia!')
