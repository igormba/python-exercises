#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.

s1 = float(input('Informe o seu salário: R$ '))
c = s1 * 15 / 100
s2 = s1+c
print(f'Você teve um aumento de 15%, que corresponde a R${c:.2f} e o seu novo salário é R${s2:.2f}')
