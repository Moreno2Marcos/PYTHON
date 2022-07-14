# https://www.youtube.com/watch?v=-QkOIHJ1Chw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=27

from random import randint

computador = randint(0, 10)
print('Sou o seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if computador == jogador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')

print('Acertou com {} tentativas. Parabéns!'.format(palpites))
