# https://www.youtube.com/watch?v=VrQmMbPpbf0&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=39


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# programa principal
print('-'*30)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
