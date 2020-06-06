'''Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.'''

from random import randint

def sorteio(lista):
    print('Sorteando os números!')
    for cont in range(0, 5):
        num = randint(1, 10)
        numeros.append(num)
        print(f'{num} ', end='')
    print('Fim!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos números pares de {lista} é {soma}.')

numeros = list()
sorteio(numeros)
somaPar(numeros)
