'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem mais de 20 anos.'''

cont18 = contm = contf = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 25)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        cont18 += 1
    if idade >= 20 and sexo == 'F':
        contf += 1
    if sexo == 'M':
        contm += 1
    if resp == 'N':
        break
print('Cadastro Finalizado!')
print(f'Você cadastrou {cont18} pessoas maiores de 18 anos.')
print(f'Ao todo, temos {contm} homens cadastrados.')
print(f'{contf} são mulheres acima de 20 anos.')