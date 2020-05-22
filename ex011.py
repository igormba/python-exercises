''''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
tinta necessaria para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m2.'''

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print(f'A sua parede tem {largura} x {altura} e sua área é de {area}m.')
tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta} l de tinta')