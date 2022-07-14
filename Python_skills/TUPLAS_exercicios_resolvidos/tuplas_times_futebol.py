# https://www.youtube.com/watch?v=RexybLcGewA&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=3

brasileirao = ('Palmeiras', 'Atlético', 'São Paulo',
               'Santos', 'Internacional', 'Goiás', 'Botafofo',
               'Corinthians', 'Flamengo', 'Athletico-PR',
               'Bahia', 'Ceará SC', 'Fluminense', 'Fortaleza',
               'Cruzeiro', 'Chapecoence', 'Avaí', 'CSA',
               'Grêmio', 'Vasco da Gama')

# PROCESSAMENTO E SAÍDA
print('-='*30)
print(f'Lista de times do Brasileirão: {brasileirao}')

# IMPRIME CADA ELEMENTO DA TUPLA EM ORDEM VERTICAL

print('-='*30)
print(f'Os 5 primeiros são {brasileirao[:5]}')
print('-='*30)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-='*30)

print(f'O Chapecoense está na {brasileirao.index("Chapecoence") + 1}ª posição')