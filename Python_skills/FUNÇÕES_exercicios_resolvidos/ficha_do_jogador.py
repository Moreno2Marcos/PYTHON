# https://www.youtube.com/watch?v=FbOvilKfHMI&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=38


def ficha(nome='<desconhecido>', gols=0):
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-'*30)
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
