'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro= Ana Último= Souza'''

nome = str(input('Informe o seu nome completo: ')).strip()
primeiro = segundo = nome.split()

print(f'O primeiro nome é {primeiro[0]}.')
print(f'O último nome é {segundo[-1]}.')