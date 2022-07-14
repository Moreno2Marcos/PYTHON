# https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=33

num = int(input('Digite um número entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(u, d, c, m))
