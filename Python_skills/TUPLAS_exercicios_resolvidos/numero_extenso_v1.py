# https://www.youtube.com/watch?v=ei2Kr3ccfO0&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=2

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break

    print('Tente novamente. ', end='')

print(f'Você digitou o número {numeros[num]}')