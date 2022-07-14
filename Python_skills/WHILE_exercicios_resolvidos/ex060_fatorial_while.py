# https://www.youtube.com/watch?v=9dlBZlkvvxY&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=29

n = int(input('Digite um número\npara calcular seu fatorial: '))

cont = n
fact = 1

print('Calculando {}! = '.format(n), end='')

while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')

    fact *= cont
    cont -= 1

print('{}'.format(fact))
