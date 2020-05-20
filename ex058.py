'''Melhore o jogo do Desafio 28 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
 tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer.'''

from random import randint
computador = randint(0, 11)
soma = 0
jogador = ''
print('Olá, sou o seu computador.')
print('Irei pensar em um número entre 0 e 10. Será que você consegue adivinhar? ')
while jogador != computador:
    jogador = int(input('Qual é o seu palpite? '))
    if jogador == computador:
        print('Você acertou! Tá mais do que de parabéns.')
    else:
        print('Você errou. Tente novamente!')
        soma += 1
print('Caramba, você precisou de {} tentativas para adivinhar. Tente ser melhor na próxima!'.format(soma))
