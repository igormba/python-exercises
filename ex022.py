#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas.
#O nome com todas as letras minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Informe o seu nome completo: ')).strip()
print('O seu nome completo é {}.'.format(nome))
print('O seu nome completo em letras maiúsculas é {}.'.format(nome.upper()))
print('O seu nome completo em letras minúsculas é {}.'.format(nome.lower()))
print('O seu nome completo possui {} letras ao todo.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))






