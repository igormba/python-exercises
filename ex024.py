# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Informe a cidade em que você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')

