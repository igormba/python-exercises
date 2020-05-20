# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0,5) # Faz o computador "Pensar"
print('-=-' * 23)
print('Vou pensar em um número de 0 a 5. Será que você consegue adivinhar?!')
print('-=-' *23)
jogador = int(input('Qual foi o número que pensei? '))
if computador == jogador:
    print('Que incrivel, você realmente acertou! Eu pensei mesmo no número {}!'.format(computador))
else:
    print('Você errou! HA HA HA O número que eu pensei foi {}!'.format(computador))
