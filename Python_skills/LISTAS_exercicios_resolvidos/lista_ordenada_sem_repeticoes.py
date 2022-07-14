# https://www.youtube.com/watch?v=QDpwjBYRcVE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=11

valores = list()

for c in range(0, 5):
    num = int(input('Digite um valor: '))

# verifica se o valor inserido é o primeiro elemento ou é maior
# que o último elemento
    if c == 0 or num > valores[-1]:
        valores.append(num)
        print('Adicionado ao final da lista...')
# -------------------------------------------
# faz um percorrido pela lista para verificar se o último valor
# inserido é menor que os anteriores e o inserta numa posição
    else:
        for pos in range(0, len(valores)):
            if num <= valores[pos]:
                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break

print('-='*30)
print(f'Os valores digitados em ordem foram {valores}')
