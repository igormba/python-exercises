# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

print('-=-' * 20)
print('Bem vindo a Escola Andrade')
print('-=-' * 20)
nome = str(input('Qual seu nome? ')).strip()
nota1 = float(input('Informe a sua primeira nota: '))
nota2 = float(input('Informe a sua segunda nota: '))
soma = (nota1 + nota2) / 2
if soma <= 5.0:
    print('Sua média final é {} e você está REPROVADO!'.format(soma))
elif soma >= 7.0:
    print('Sua média final é {} Você está APROVADO. PARABÉNS!'.format(soma))
else:
    print('Sua média final é {} e você está na RECUPERAÇÃO.'.format(soma))
print('Tenha um ótimo dia! ')