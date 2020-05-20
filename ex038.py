# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela a mensagem:
# - O primeiro valor é maior.
# - O segundo valor é maior.
# - Não existe valor maior, os dois são iguais.

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num1 > num2:
    print('O primeiro número escolhido {} e ele tem o valor maior que o segundo número que é {}.'.format(num1, num2))
elif num2 > num1:
    print('O segundo número escolhido {} e ele tem o valor maior que o primeiro número que é {}.'.format(num2, num1))
else:
    print('Como o primeiro número é {} e o segundo número também é {}, não existe valor maior, os dois são iguais.'.format(num1, num2))