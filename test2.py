precos = [100, 500, 10, 25]
impostos = []
for preco in precos:
    impostos.append((lambda x: x * .3)(preco))
print(impostos)