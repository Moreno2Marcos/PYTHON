# https://www.youtube.com/watch?v=5yKiud-YNaE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=26

partidas = list()
jogador = dict()

jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador[\nome\]} jogou? '))
for c in range(0, tot):
	partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas  # não é necessário receber uma copia de partidas[:] porque vai ser lidos os dados de um jogador só!
jogador['total'] = sum(partidas)

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
	print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador[\nome\]} jogou {len(jogador[\gols\])} partidas.')
for i, v in enumerate(jogador['gols']):
	print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador[\total\]} gols.')
