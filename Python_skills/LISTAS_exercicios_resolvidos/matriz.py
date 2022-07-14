# https://www.youtube.com/watch?v=EGmlFdwD4C4&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=18

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # é uma matriz 3x3 (já sei o número de elementos!)
                                            # se preenche de zeros para precisar usar o método append()

# Cria matriz
for l in range(0, 3):  # l: linha
    for c in range(0, 3):  # c: coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

# Visualiza matriz
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
