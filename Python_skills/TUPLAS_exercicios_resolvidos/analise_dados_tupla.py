# https://www.youtube.com/watch?v=1u7oA8ckjAc&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=5

valores = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram: ', end='')
for ele in valores:
    if ele % 2 == 0:
        print(ele, end=' ')
