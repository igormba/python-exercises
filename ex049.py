'''Rafaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for tabu in range(0, 11):
    print('{} x {:2} = {}'.format(n, tabu, n*tabu))
print('-' * 12)