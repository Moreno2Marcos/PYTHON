# https://www.youtube.com/watch?v=Kbs97l38vVQ&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=40


def notas(*notas, sit=False):  # cabecalho da funcao!!!
    """
    ->Função para analisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    turma = dict()

    turma['total'] = len(notas)

    maximo = minimo = 0
    for c in range(0, len(notas)):
        if c == 0:
            maximo = minimo = notas[c]
        else:
            if notas[c] > maximo:
                maximo = notas[c]
            if notas[c] < minimo:
                minimo = notas[c]
    turma['maior'] = maximo
    turma['menor'] = minimo

    turma['média'] = sum(notas) / len(notas)

    if sit:
        if turma['média'] < 5:
            turma['situação'] = 'RUIM'
        elif 5 <= turma['média'] < 7:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'BOA'

    return turma


# programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
