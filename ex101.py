'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos, o voto é OPCIONAL!'
    elif idade < 16:
        return f'Com {idade} anos, ainda não vota!'
    elif idade >= 18:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO!'

ano = int(input('Ano de Nascimento: '))
print(voto(ano))