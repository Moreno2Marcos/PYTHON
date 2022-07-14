from random import randint
from time import sleep

print('\\033[33m-=-\\033[m'*20)
print('\\033[34mVou pensar em um número entre 0 e 5. Tente adivinhar...\\033[m')
print('\\033[33m-=-\\033[m'*20)

jogador = int(input('Digite um número entre 0 e 5: '))  # O jogador tenta adivinhar
computador = randint(0, 5)  # Faz o computador \PENSAR\

print('\\033[35mPROCESSANDO...\\033[m')
sleep(3)

if jogador == computador:
	print('\\033[33mPARABÉNS! Você conseguiu me vencer!\\033[m')
else:
	print('\\033[31mGANHEI! Eu pensei no número {} e não no {}!\\033[m'.format(computador, jogador))
