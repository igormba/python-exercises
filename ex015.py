# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar. Sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
print('Para calculo do valor final do aluguel, favor informar:')
Dias = int(input('Informe a quantidade de dias: '))
KM = float(input('Informe a quantidade de KMs rodados:'))
c1 = Dias * 60
c2 = KM * 0.15
print('O veiculos foi alugado por {:.0f} dias e com o total de {:.0f} KMs rodados.\nO valor final a ser pago é R$ {:.2f}'.format(Dias, KM, (c1 + c2)))