# https://www.youtube.com/watch?v=dvhP41Z7TLk&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=14

exp = str(input('Digite a expressão: '))

contA = contF = 0

for c in exp:
    if c == '(':
        contA += 1
    elif c == ')':
        contF += 1

if contA == contF:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
