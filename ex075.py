'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

numeros = tuple(int(input('Informe um número: ')) for c in range(4))
print(f'Você digitou os números: {numeros}')
print(f'Você digitou {numeros.count(9)} vezes o número 9.')
if 3 in numeros:
    print(f'O número 3 foi digitado na {numeros.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitado foram ', end= ' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')












