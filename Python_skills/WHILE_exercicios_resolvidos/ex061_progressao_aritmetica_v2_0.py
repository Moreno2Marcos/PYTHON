# https://www.youtube.com/watch?v=vu5ehetQGe8&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=30

print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

termo = primeiro
cont = 1

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
