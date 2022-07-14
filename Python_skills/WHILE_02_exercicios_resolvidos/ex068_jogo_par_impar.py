# https://www.youtube.com/watch?v=EIzgKCCDdc0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=38

from random import randint

vitoria = 0

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)

while True:

    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))

    total = computador + jogador

    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    print('-'*15)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-'*15)

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitoria += 1
        else:
            print('Você PERDEU!')
            break

    print('Vamos jogar novamente...')

print('=-'*15)
print(f'GAME OVER! Você venceu {vitoria} vezes.')
