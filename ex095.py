'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

time = list()
dados = dict()
gols = list()

while True:
    dados.clear()
    dados['Jogador'] = str(input('Nome do Jogador: '))
    dados['Gols'] = list()
    dados['Jogos'] = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))
    for c in range(0, dados["Jogos"]):
        dados['Gols'].append(int(input(f'Quantos gols na partida {c+1} ? ')))
        dados['Total de Gols'] = sum(dados['Gols'])
    while True:
        continuar = str(input('Adicionar mais um jogadores? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Informe S ou N.')
    time.append(dados.copy())
    dados.clear()
    if continuar == 'N':
        break
print('=' * 30)
print(f'{"COD":<}{" NOME":<}{"GOLS":^17}{"TOTAL":>}')
print('=' * 30)
for k, v in enumerate(time):
    print(f' {k:<3}{v["Jogador"]:<9}{str(v["Gols"]):<14}{v["Total de Gols"]}')
print('=' * 30)
while True:
    escolha = int(input('Informe o codigo do jogador para analise: (999 finaliza) '))
    if escolha == 999:
        break
    elif escolha not in range(0, len(time)):
        print('Erro! Escolha o número correspondente ao jogador.')
    else:
        print(f'Informações do jogador {time[escolha]["Jogador"]}.')
        for k, v in enumerate(time[escolha]['Gols']):
            print(f'No jogo {k+1} fez {v} gols.')
    print('=' * 30)
print('PROGRAMA FINALIZADO!')