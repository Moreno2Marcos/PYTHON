# https://www.youtube.com/watch?v=84jUX96cs7Q&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=37


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número num.
    Autor: Iván Moreno
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c

    return f


print('-'*30)
print(fatorial(5, show=True))
help(fatorial)
