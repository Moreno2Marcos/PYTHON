# https://www.youtube.com/watch?v=-OnqSGh0u4g&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=19

primeiro_termo = int(input('Escreva o primeiro termo da PA: '))
razao = int(input('Escreva a razão da PA: '))

decimo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo + razao, razao):
    print('{} '.format(c), end='-> ')

print('ACABOU')
