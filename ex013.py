#Faça um algoritmo que leia o salário de um funcionario e mostre seu novo salário, com 15% de aumento.
s1 = float(input('Informe o seu salário: R$'))
c = s1*15/100
s2 = s1+c
print('Você teve um aumento de 15% que corresponde a R$ {:.2f} e o seu novo salário é: R$ {:.2f}'.format(c, s2))
