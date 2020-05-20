# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai curtar R$7,00 por cada Km acima do limite.

velocidade = int(input('Informe a velocidade do veiculo: '))
if velocidade >= 80:
    print('Você foi multado! Você excedeu o limite permitido pela via.')
    r = (velocidade - 80) * 7
    print('A multa a ser paga é de R${:.2f}'.format(r))
else:
    print('Velocidade permitida pela via! Boa viagem!')
