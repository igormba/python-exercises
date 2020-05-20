'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
maior = 0
opcao = 0
while opcao != 5:
    sleep(0.5)
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do Programa''')
    opcao = int(input('Escolha uma opção: '))
    sleep(0.5)
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} é igual a {}.'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('A multiplicação de {} e {} é igual a {}.'.format(num1, num2, mult))
    if opcao == 3:
        num1 > maior
        maior = num1
        if num2 > maior:
            maior = num2
            print('O maior número digitado é {}.'.format(maior))
        if num1 == num2:
            print('Os valores são iguais.')
    elif opcao == 4:
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Programa finalizado!')
    else:
        print('A opção escolhida é invalida. Digite novamente!')