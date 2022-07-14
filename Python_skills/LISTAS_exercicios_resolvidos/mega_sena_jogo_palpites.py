# https://www.youtube.com/watch?v=Hd7Ycaj61xE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=20

from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)

numero_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

jogos = list()
palpites = list()

for c in range(0, numero_jogos):
    # verifica que os numeros aleatorios nao se repitam dentro de uma mesma lista!
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    palpites.append(jogos[:])
    jogos.clear()

print('-='*3, f'SORTEANDO {numero_jogos} JOGOS', '-='*3)
for i, j in enumerate(palpites):
    print(f'Jogo {i+1}: {j}')
    sleep(1)
print('-='*5, f'< BOA SORTE! >', '-='*5)
