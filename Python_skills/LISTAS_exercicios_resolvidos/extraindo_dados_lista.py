# https://www.youtube.com/watch?v=SXJKAVVlvGA&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=12

numeros = list()

while True:
    numeros.append(int(input('Digite um número: ')))

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print(f'Ao todo foram digitados {len(numeros)} números.')

numeros.sort(reverse=True)
print(f'A lista ordenada de forma decrescente: {numeros}')

if 5 in numeros:
    print(f'O valor 5 faz parte da lista! e foi digitado nas posições: ', end='')
    for c, v in enumerate(numeros):
        if 5 == v:
            print(f'{c}...', end='')
else:
    print(f'O valor 5 não foi encontrado na lista!')
