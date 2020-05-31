'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
O primeiro valor é maior.
O segundo valor é maior.
Não existe valor maior, os dois são iguais.'''

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num1 > num2:
    print(f'O primeiro número escolhido é {num1} e ele tem o valor maior que o segundo número que é {num2}.')
elif num2 > num1:
    print(f'O segundo número escolhido é {num2} e ele tem o valor maior que o primeiro número que é {num1}.')
else:
    print(f'Como o primeiro número é {num1} e o segundo número também é {num2}, não existe valor maior, os dois são iguais.')