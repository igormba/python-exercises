# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

print('-=-' * 14)
print('Olá, seja bem-vindo a calculadora de IMC.')
print('-=-' * 14)
nome = str(input('Qual seu nome: '))
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
calculo = peso / (altura ** 2)
if calculo < 18.5:
    print('{}, como você tem {}mm de altura e pesa {}kg, o seu IMC é {:.2f}.'.format(nome, altura, peso, calculo))
    print('Você está abaixo do peso ideal.')
elif calculo >= 18.5 and calculo < 25:
    print('{}, como você tem {}m de altura e pesa {}kg, o seu IMC é {:.1f}.'.format(nome, altura, peso, calculo))
    print('Você tem o peso ideal.')
elif calculo >= 25 and calculo < 30:
    print('{}, como você tem {}m de altura e pesa {}kg, o seu IMC é {:.1f}.'.format(nome, altura, peso, calculo))
    print('Você tem sobrepeso.')
elif calculo >= 30 and calculo <= 40:
    print('{}, como você tem {}m de altura e pesa {}kg, o seu IMC é {:.1f}.'.format(nome, altura, peso, calculo))
    print('Você tem Obesidade!')
elif calculo > 40:
    print('{}, como você tem {}m de altura e pesa {}kg, o seu IMC é {:.1f}.'.format(nome, altura, peso, calculo))
    print('Você tem Obesidade Mórbida!')