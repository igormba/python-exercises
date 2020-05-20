'''Escreva um progrma que leia um n inteiro qualquer e mostra na tela os n primeiros elementos de uma sequencia de Fibonacci.
Ex: 0 1 1 2 3 5 8'''

n = int(input('Informe um número: '))
t1 = 0
t2 = 1
print('{} > {}'.format(t1, t2), end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' >  {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('> FIM!')