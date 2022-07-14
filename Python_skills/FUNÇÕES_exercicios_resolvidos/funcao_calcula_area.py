# https://www.youtube.com/watch?v=oV1s53YGtvE&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=30


def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')


# programa principal
print('\nControle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
