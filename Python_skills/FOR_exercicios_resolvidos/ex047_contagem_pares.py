# https://www.youtube.com/watch?v=Qws8-E-YrlY&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=15

print('Números pares no intervalo de 1 e 50:')

for c in range(2, 51, +2):  # Aqui faco 25 iteracoes a pasos de 2 em 2
    if c != 50:
        print(c, end=', ')
    else:
        print(c)
#print()
#for c in range(1, 51):  # Faz mais repeticoes das necessarias (o dobro)! (faco 50 iteracoes!)
#    if c % 2 == 0:
#        print(c, end=', ')