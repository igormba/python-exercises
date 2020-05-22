# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
#n = int(input('Informe um nÚmero:'))
#d = n * 2
#t = n * 3
#rz = n ** (1/2)
#print('O número escolhido é {}, o seu dobro é {}, seu triplo {} e a sua raiz quadrada é {:.2}! '.format(n, d, t, rz))
#print('Obrigado e até a próxima! ')

n = int(input('Informe um número: '))
#print('O número escolhido é {}, o seu dobro é {}, seu triplo {} e a sua raiza quadrada é {:.2}!'.format(n, (n*2), (n*3), (n**(1/2))))
print('O número escolhido é {}, o seu dobro é {}, seu triplo {} e a sua raiza quadrada é {:.2}!'.format(n, (n*2), (n*3), pow(n, (1/2))))
print('Obrigado e até a próxima!')