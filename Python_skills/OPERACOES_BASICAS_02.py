# define os precos
precoA = 1.10
precoB = 3.03
precoC = 2.79
# define os custos
custoA = 1.16
custoB = 4.32
custoC = 2.94
# define quantidades
qtdA = 63
qtdB = 21
qtdC = 93
# calcula lucro total
lucA = (precoA * qtdA) - (custoA * qtdA)
lucB = (precoB * qtdB) - (custoB * qtdB)
lucC = (precoC * qtdC) - (custoC * qtdC)
lucTot = lucA + lucB + lucC
print('Lucro total da loja R$', lucTot)
# faturamento total
faTot = (precoA * qtdA) + (precoB * qtdB) + (precoC * qtdC)
print('Faturamento total da loja R$', faTot)
# calcula custo total
cusTot = (custoA * qtdA) + (custoB * qtdB) + (custoC * qtdC)
print('Custo total da loja R$', cusTot)