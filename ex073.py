'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.'''

times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
         'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro',
         'CSA', 'Chapecoense', 'Avaí')

print(f'5 primeiros colocados da tabela: {times[0:5]}')
print(f'4 últimos colocados da tabela: {times[16:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição.')