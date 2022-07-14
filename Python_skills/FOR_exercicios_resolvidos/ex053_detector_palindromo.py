# https://www.youtube.com/watch?v=5VBWe6BXzRo&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=21

frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = junto[::-1]  # Pega de tras para frente!!! (essa eh a logica central da resolucao!

print('O inverso de {} é {}'.format(junto, inverso))

if junto == inverso:
    print('é palíndromo!')
else:
    print('Não é palíndromo')
