# define os produtos, precos e quantidades
produtos = ['A', 'B', 'C']
precos = [147.3, 75.4, 35.7]
quantidades = [23, 14, 7]
# itera e multiplica cada preco com sua quantidade
pos = 0
for preco in precos:
    # mostra o resultado
    print('O Faturamento do Produto {} é de R$ {:.2f}'.format(produtos[pos], preco * quantidades[pos]))
    pos = pos + 1