# https://www.youtube.com/watch?v=23UOVEetNPY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=36

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" aparece {} vez(es)'.format(frase.count('A')))
print('A letra "A" aparece na posição {} por primeira vez!'.format(frase.find('A') + 1))
# rfind: procura a partir do lado direito (de derecha a izquierda)
print('A letra "A" aparece na posição {} por última vez!'.format(frase.rfind('A') + 1))
