# https://www.youtube.com/watch?v=vp9UX7wr92o&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=33

from time import sleep


def maior(* numeros):
    max = 0

    print('-='*30)
    print('Analisando os valores passados...')

    for pos, num in enumerate(numeros):
        print(f'{num}', end=' ')
        sleep(0.3)

        if pos == 0:
            max = num
        else:
            if num > max:
                max = num

    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {max}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
