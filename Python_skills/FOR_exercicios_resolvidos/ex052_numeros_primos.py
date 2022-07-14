# https://www.youtube.com/watch?v=Er5Hyd4LyVw&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=20

num = int(input('Escreva um número inteiro: '))

tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\033[m\nO número {} foi divisível {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO')