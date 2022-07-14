# https://www.youtube.com/watch?v=q8Z1cRdJnfk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=9

valores = list()
mai = men = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))

    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]

print('-='*30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')
print()
