# https://www.youtube.com/watch?v=czDcimdc3GU&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=36

# ESCOPO DE IMPORTACAO!
#from datetime import date  # a classe foi importada para
                           # o programa inteiro!
                           # importacao global!


def voto(ano):
    from datetime import date  # importacao local!
                               # economiza memoria?
                               # tempo de execução?
                               # caso a classe date só
                               # seja usado dentro da funcao!
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL.'


# Programa principal
print('-'*30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
