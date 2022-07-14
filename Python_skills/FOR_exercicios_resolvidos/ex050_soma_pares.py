# https://www.youtube.com/watch?v=rJaBLOW57Jg&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=18

soma_pares = 0
cont_pares = 0

for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma_pares += num
        cont_pares += 1

print('Você informou {} números PARES e a total foi {}'.format(cont_pares, soma_pares))
