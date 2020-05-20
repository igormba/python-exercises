# Elabore um programa que calcule o valor de um produto, considerando o seu preço normal e condições de pagamento:
# A vista dinheiro/cheque: 10% de desconto
# A vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juros

from time import sleep
print('-=-' * 6)
print('Andrade Magazine!')
print('-=-' * 6)
print('Meu nome é Marcele e estou aqui para te auxiliar.')
nome = str(input('Qual o seu nome? ')).strip()
produto = float(input('Informe o valor do produto desejado: R$ '))
print('Temos algumas opções especiais para pagamento.', end=' ')
print('Favor escolher a que mais te agrada!')
sleep(2)
print('[ 1 ] - A vista dinheiro/cheque: 10% de desconto.')
print('[ 2 ] - A vista no cartão: 5% de desconto.')
print('[ 3 ] - Em até 2x no cartão: Preço normal.')
print('[ 4 ] - 3x ou mais no cartão: 20% de juros.')
anunciado = int(input('Escolha uma opção de pagamento: '.format(nome)))
op1 = produto - (produto * 10 / 100)
op2 = produto - (produto * 5 / 100)
op3 = produto
op4 = (produto * 20 / 100) + produto
if anunciado == 1:
    print('{}, o seu produto de acordo com a opção de pagamento escolhida, tem o valor final de R$ {:.2f}'.format(nome, op1))
elif anunciado == 2:
    print('{}, o seu produto de acordo com a opção de pagamento escolhida, tem o valor final de R$ {:.2f}'.format(nome, op2))
elif anunciado == 3:
    print('{}, infelizmente na opção escolhida, não fornecemos nenhum nivel de desconto e o valor final do seu produto continua o mesmo, R$ {:.2f}'.format(nome, op3))
elif anunciado == 4:
    print('{}, o seu produto de acordo com a opção de pagamento escolhida, tem o valor final de R$ {:.2f}'.format(nome, op4))
else:
    print('{}, a opção escolhida é invalida. Tente novamente!'.format(nome))

