'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista. No final, mostre qual foi o valor maior e o menor valor digitado e as suas respectivas posições'''

num = list()
for n in range(0, 5):
    num.append(int(input(f'Informe um valor para a posição {n}: ')))
print(f'Os valores {num} foram inseridos na lista.')
print(f'O maior valor digitado é {max(num)}, na posição {num.index(max(num))} e o menor valor é {min(num)}, na posição {num.index(min(num))}.')
