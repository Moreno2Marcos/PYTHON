# https://www.youtube.com/watch?v=w7yn1_Mfu0E&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=32

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input('Quntos termos você quer mostrar? '))

t1 = 0
t2 = 1

print('~' * 30)
print('{} -> {}'.format(t1, t2), end='')

cont = 3

while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

print(' -> FIM')
print('~' * 30)
