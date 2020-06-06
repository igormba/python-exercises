'''Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva('Olá, mundo!')
Saida:
-----------
Olá, mundo!
-----------'''

def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f' {txt}')
    print('-' * tam)

escreva(str(input('Escreva o titulo: ')))

