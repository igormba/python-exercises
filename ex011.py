#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
#tinta necessaria para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.
largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura * altura
print('A sua parede tem {} x {} e sua área é de {}m.'.format(largura, altura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))