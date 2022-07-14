# https://www.youtube.com/watch?v=uk0gDFQEo_I&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=13

numeros = list()
pares = list()
impares = list()

while True:
    numeros.append(int(input('Digite um número: ')))

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

for c in numeros:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'Lista de números completa {numeros}')
print(f'Lista de números pares {pares}')
print(f'Lista de números ímpares {impares}')
