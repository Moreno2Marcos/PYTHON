# https://www.youtube.com/watch?v=dvhP41Z7TLk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=14

exp = str(input('Digite a expressão: '))

pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
