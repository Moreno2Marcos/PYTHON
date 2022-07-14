# https://www.youtube.com/watch?v=2-fy24bbMJ4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=17

num = [[], []]  # cria uma lista vacia com duas listas internas vacias!
                # uma lista interna para os PARES outra para os IMPARES
                # dessa maneira se satisfaz a condição de usar uma única
                # lista!

valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))

    if valor % 2 == 0:
        num[0].append(valor)  # escolhi que a primeira lista interna fosse para pares
    else:
        num[1].append(valor)  # escolge que a segunda lista interna fosse para ímpares

num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
