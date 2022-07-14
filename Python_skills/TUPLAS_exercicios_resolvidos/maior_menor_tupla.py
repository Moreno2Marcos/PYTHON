# https://www.youtube.com/watch?v=mlwt2CRQkTQ&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=4

from random import randint

aleatorios = (randint(1, 10), randint(1, 10),
              randint(1, 10), randint(1, 10),
              randint(1, 10))

print('Os valores sorteados foram:', end=' ')
for ele in aleatorios:
    print(f'{ele} ', end='')

print(f'\nO maior valor sorteado: {max(aleatorios)}')
print(f'O menor valor sorteado: {min(aleatorios)}')