# https://www.youtube.com/watch?v=QtElJDa9ICM&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=17

n = int(input('Digitar um número para ver sua tabuada: '))

for c in range(1, 11):
    print('{} X {:2} = {}'.format(n, c, n*c))