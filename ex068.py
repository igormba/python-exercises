'''Faça um programa que jogue PAR ou IMPAR com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
computador = randint(0, 10)
cont = 0
print('=-' * 13)
print('VAMOS JOGAR PAR OU IMPAR!')
print('=-' * 13)
while True:
    n = int(input('Escolha um número: '))
    e = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    if (computador + n) % 2 == 0 and e == 'P':
        print(f'Você escolheu o número {n} e o computador o número {computador}.')
        print(f'Total de {n + computador}. PAR ganhou!')
        cont += 1
    elif (computador + n) % 2 == 1 and e == 'P':
        print(f'Você escolheu o número {n} e o computador o número {computador}.')
        print(f'Total de {n + computador}. ÍMPAR ganhou!')
        break
    elif (computador + n) % 2 == 0 and e == 'I':
        print(f'Você escolheu o número {n} e o computador o número {computador}.')
        print(f'Total de {n+computador} PAR ganhou!')
        break
    else:
        print(f'Você escolheu o número {n} e o computador o número {computador}.')
        print(f'Total de {n+computador} ÍMPAR ganhou!')
        cont += 1
    print('Você VENCEU! Vamos jogar novamente!')
print(f'Você PERDEU! \n\nVocê venceu o computador {cont} vezes.')
