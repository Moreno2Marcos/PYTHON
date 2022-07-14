# https://www.youtube.com/watch?v=LkAzRnc_GPk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=10

valores = list()

while True:

    num = int(input('Digite um valor: '))

    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('-='*30)
valores.sort()
print(f'Você digitou os valores {valores}')
