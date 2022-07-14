# https://www.youtube.com/watch?v=cwrqIztaAwk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=24

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
		'jogador2': randint(1, 6),
		'jogador3': randint(1, 6),
		'jogador4': randint(1, 6)}

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('Valores sorteados:')
for k, v in jogo.items():
	print(f'O {k} tirou {v} no dado.')
	sleep(1)
print('-='*30)
print('  == RANKING DOS JOGADORES ==')
for pos, v in enumerate(ranking):
	print(f'   {pos+1}° lugar: {v[0]} com {v[1]}.')
	sleep(1)