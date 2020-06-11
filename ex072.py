'''Crie um progrma que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero a vinte. Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
escolha = ' '
escolha = int(input('Escolha um número de 0 a 20: '))
while escolha not in range(0, 21):
    escolha = int(input('Escolha um número de 0 a 20: '))
print(f'Você escolheu o número {numeros[escolha]}.')