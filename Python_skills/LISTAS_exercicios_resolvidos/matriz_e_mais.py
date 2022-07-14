# https://www.youtube.com/watch?v=QhS829x6up4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=19

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # é uma matriz 3x3 (já sei o número de elementos!)
                                            # se preenche de zeros para precisar usar o método append()

soma_pares = soma_terceira_coluna = maior_segunda_coluna = 0

for l in range(0, 3):  # l: linha
    for c in range(0, 3):  # c: coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]

        if c == 2:
            soma_terceira_coluna += matriz[l][2]

        if l == 1:
            maior_segunda_coluna = matriz[1][c]
        elif matriz[1][c] > maior_segunda_coluna:
            maior_segunda_coluna = matriz[1][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_segunda_coluna}')
