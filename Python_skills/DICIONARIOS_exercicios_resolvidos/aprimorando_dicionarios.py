# https://www.youtube.com/watch?v=mw1So0r317Y&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=28

partidas = list()
jogador = dict()
teme = list()

while True:
	jogador.clear()
	jogador['nome'] = str(input('Nome do Jogador: '))
	tot = int(input(f'Quantas partidas {jogador[\nome\]} jogou? '))
	partidas.clear()
	for c in range(0, tot):
		partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
	jogador['gols'] = partidas[:]
	jogador['total'] = sum(partidas)
	teme.append(jogador.copy())
	while True:
		resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
		if resp in 'NS':
			break
		print(f'ERRO! Responda apenas S ou N.')
	if resp == 'N':
		break

print('-='*30)
print('cod ', end='')
for i in jogador.keys():
	print(f'{i:<15}', end='')
print()
print('-'*40)
for pos, jog in enumerate(teme):
	print(f'{pos:>3} ', end=' ')
	for v in jog.values():
		print(f'{str(v):<15}', end='')
	print()
print('-'*40)
while True:
	busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
	if busca == 999:
		break
	if busca >= len(teme):
		print(f'ERRO! Não existe jogador com código {busca}!')
	else:
		print(f' -- LEVANTAMENTO DO JOGADOR {teme[busca][\nome\]}:')
		for pos, part in enumerate(teme[busca]['gols']):
			print(f'    No jogo {pos + 1} fez {part} gols.')
	print('-' * 40)
print('<< VOLTE SEMPRE >>')