#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro= Ana Último= Souza

nome = str(input('Informe o seu nome completo: ')).strip()
primeiro = nome.split()
segundo = nome.split()
print('O primeiro nome é {}.'.format(primeiro[0]))
print('O último nome é {}.'.format(segundo[-1]))