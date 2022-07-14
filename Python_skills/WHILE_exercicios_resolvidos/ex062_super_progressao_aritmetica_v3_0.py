# https://www.youtube.com/watch?v=BWAWq7n6PCk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=31

print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1
total = 0
mais =10

while mais != 0:
    total += mais

    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total))
