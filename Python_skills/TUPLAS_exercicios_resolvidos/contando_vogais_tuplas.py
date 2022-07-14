# https://www.youtube.com/watch?v=8BgSqrOpKvU&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=7

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')

    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
