# https://www.youtube.com/watch?v=tapTa6KVG-A&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=12

from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))

if jogador == 0 or jogador == 1 or jogador == 2:
	print('JO')
	sleep(1)
	print('KEN')
	sleep(1)
	print('PO!!!')
	sleep(1)

	print('-=' * 14)
	print('  ' + 'Computador jogou {}'.format(itens[computador]))
	print('  ' + 'Jogador jogou {}'.format(itens[jogador]))
	print('-=' * 14)

	if computador == 0:
		if jogador == 0:
			print('EMPATE')
		elif jogador == 1:
			print('JOGADOR VENCE')
		elif jogador == 2:
			print('COMPUTADOR GANHOU')
	elif computador == 1:
		if jogador == 0:
			print('COMPUTADOR GANHOU')
		elif jogador == 1:
			print('EMPATE')
		elif jogador == 2:
			print('JOGADOR VENCE')
	elif computador == 2:
		if jogador == 0:
			print('JOGADOR VENCE')
		elif jogador == 1:
			print('COMPUTADOR GANHA')
		elif jogador == 2:
			print('EMPATE')
else:
	print('JOGADA INVÁLIDA!')