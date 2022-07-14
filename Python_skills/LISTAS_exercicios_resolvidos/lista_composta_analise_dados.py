# https://www.youtube.com/watch?v=zPtvuLiEdKk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=16

galera = list()  # lista principal, princ = []
dados = list()  # lista temporaria, temp = []
maxi = mini = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(galera) == 0:
        maxi = mini = dados[1]
    else:
        if dados[1] > maxi:
            maxi = dados[1]
        if dados[1] < mini:
            mini = dados[1]

    galera.append(dados[:])
    dados.clear()

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(galera)} pessoas.')

print(f'O maior peso foi de {maxi}kg. Peso de ', end='')
for p in galera:
    if p[1] == maxi:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {mini}kg. Peso de ', end='')
for p in galera:
    if p[1] == mini:
        print(f'[{p[0]}]', end=' ')
print()
