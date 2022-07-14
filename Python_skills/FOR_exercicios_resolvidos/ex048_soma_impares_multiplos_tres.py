# https://www.youtube.com/watch?v=iHjsUxNA-wo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=16

s = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print('A total dos impares que são múltiplos de 3, no intervalo de 1 até 500 é: {}'.format(s))
print('A total de todos os {} valores solicitados é {}'.format(cont, s))