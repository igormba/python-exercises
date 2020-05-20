# Escreva um programa que pergunte o salário de um funcionario e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o seu salario: '))
if salario >= 1250.00:
    s1 = (salario*10/100) + salario
    print('O seu salario anterior era de R${:.2f} e com o aumento de 10% foi para R${:.2f}'.format(salario, s1))
else:
    s2 = (salario*15/100) + salario
    print('O seu salario anterior era de R${:.2f} e com o aumento de 15% foi para R${:.2f}'.format(salario, s2))