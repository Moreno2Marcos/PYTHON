# define conj. de faturamentos
fatMens = [189351, 191231, 120575, 151688]
# itera a list 2 a 2 elementos
MOM = []
for fat in range(1, len(fatMens)):
    # calcula o MOM atual
    mom = round(((fatMens[fat] - fatMens[fat-1]) / fatMens[fat-1]) * 100, 2)
    # adiciona o MOM na lista
    MOM.append(mom)
# visualiza os resultados
MOM