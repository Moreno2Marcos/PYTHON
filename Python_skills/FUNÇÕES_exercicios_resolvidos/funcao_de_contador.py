# https://www.youtube.com/watch?v=DCBlt_z2UOE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=32

from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1

    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c}', end=' ')
            c += passo
            sleep(0.5)
        print('FIM!')
    else:
        c = inicio
        while c >= fim:
            print(f'{c}', end=' ')
            c -= passo
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))

contador(i, f, p)
