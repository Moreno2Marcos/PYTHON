# https://www.youtube.com/watch?v=d2ug6quC1bk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=36

cont = soma = 0

while True:
    n = int(input('Digite um valor (999 para parar): '))

    if n == 999:
        break

    cont += 1
    soma += n

print(f'A total dos {cont} valores foi {soma}!')
