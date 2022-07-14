# https://www.youtube.com/watch?v=X0a5aZg93Uc&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=37

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)

    if n < 0:
        break

    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')

    print('-'*30)

print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
