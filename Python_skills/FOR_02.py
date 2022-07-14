# define os produtos, precos e quantidades
produtos = ['A', 'B', 'C']
precos = [147.3, 75.4, 35.7]
quantidades = [23, 14, 7]
# itera e multiplica cada preco com sua quantidade
pos = 0
for preco in precos:
    # verifica se o faturamento de cada produto atingiu a meta
    if (preco * quantidades[pos]) > 1000:
        print('O produto {} atingiu o faturamento!'.format(produtos[pos]))
    else:
        print('O produto {} não atingiu o faturamento!'.format(produtos[pos]))
    pos = pos + 1