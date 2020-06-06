'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from random import sample
from time import sleep
def maior(txt):
    print('-=' * 30)
    print('Analisando os números...')
    contador = len(txt)
    maior = max(txt)
    sleep(1)
    print(f'{txt} Foram informados {contador} números ao todo.')
    print(f'O maior número é {maior}.')


maior(sample(range(0, 100),6))
maior(sample(range(0, 100),3))
maior(sample(range(0, 100),2))
maior(sample(range(0, 100),1))


