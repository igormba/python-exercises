'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

dados = dict()
gols = list()

dados['Jogador'] = str(input('Nome do Jogador: '))
dados['Jogos'] = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))

for c in range(dados["Jogos"]):
    gols.append(int(input(f'Quantos Gols foram feitos na {c + 1}ª partida? ')))
    dados['Gols'] = gols[:]

print('-=-' * 30)
print(dados)
print('-=-' * 30)

print(f'O nome do jogador é {dados["Jogador"]}.')
print(f'{dados["Jogador"]} fez {sum(gols)} gols em {dados["Jogos"]} partidas.')


