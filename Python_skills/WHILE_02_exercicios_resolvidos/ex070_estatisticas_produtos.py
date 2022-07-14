# https://www.youtube.com/watch?v=hS8QdW-1HTo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=40

print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)

total = contMil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))

    cont += 1
    total += preco

    if preco > 1000:
        contMil += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi \033[7;30mR${total:.2f}\033[m')
print(f'Temos {contMil} produtos custando mais de \033[7;30mR$1000.00\033[m')
print(f'O produto mais barato foi \033[7;30m{barato}\033[m que custa \033[7;30mR${menor:.2f}\033[m')