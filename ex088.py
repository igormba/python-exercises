'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import sample
from time import sleep
jogos = []
num = int(input('Quantos jogos você quer gerar? '))
for c in range(num):
    sorteio = sorted(sample(range(1, 61), 6))
    jogos.append(sorteio[:])
    print(f'Jogo {c + 1}: {sorteio}')
    sleep(0.5)
print('-=' * 30)
print(f'Sorteio dos {num} jogos concluido.')
    

