# Escreva um programa que converta uma temperatura digitada em Cº e converta em ºF.
temperatura = float(input('Informe a temperatura: Cº'))
calculo = (temperatura * 1.8) + 32
print('A temperatura convertida de Celsius para Fahrenheit é: ºF {:.0f}'.format(calculo))