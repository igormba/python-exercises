'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separado os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.'''

lista = [[], []]
for c in range(1, 8):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print(f'Os números pares são {sorted(lista[0])}.')
print(f'Os números impares são {sorted(lista[1])}.')

