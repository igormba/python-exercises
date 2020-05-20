#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto = float(input('Informe o valor do produto: R$'))
desconto = produto - (produto*5/100)
print('O seu produto com descontos, tem o valor final de: RS {:.2f}'.format(desconto))