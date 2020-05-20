#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

print('Olá, escolha um número, pra que eu te mostre o seu número sucessor e antecessor. Vamos lá?!')
n = int(input('Digite um número: '))
print('Você escolheu o número {}, seu sucessor é o número {} e o seu antecessor é o número {}.'.format(n, (n+1), (n-1)))
print('Obrigado e até a próxima! ')