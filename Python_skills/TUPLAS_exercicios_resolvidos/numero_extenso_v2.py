# https://www.youtube.com/watch?v=ei2Kr3ccfO0&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=2

numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'catorze',
           'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

resposta = ' '
while resposta != 'N':
    num = int(input('Digite um número entre 0 e 20: '))
    while not 0 <= num <= 20:
        num = int(input('Tente novamente. Digite um '
                        'número entre 0 e 20: '))

    print(f'Você digitou o número {numeros[num]}')

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
