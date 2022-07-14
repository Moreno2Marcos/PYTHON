# https://www.youtube.com/watch?v=mYlbttiLHM0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=33

n = cont = soma = 0

n = int(input('Digite um número [999 para parar]: '))

while n != 999:
    cont += 1
    soma += n

    n = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))
