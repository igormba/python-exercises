'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual é a soma entre eles, desconsiderando
a flag.'''

n = s = qt = 0
while True:
    n = int(input('Digite um número: [PARA PARAR, DIGITE 999] '))
    if n == 999:
        break
    s += n
    qt += 1
print(f'Você digitou {qt} números e a sema entre eles é {s}.')