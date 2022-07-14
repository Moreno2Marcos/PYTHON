from math import factorial

n = int(input('Digite um número\npara calcula seu fatorial: '))

f = factorial(n)

print('O fatorial de {} é {}.'.format(n, f))