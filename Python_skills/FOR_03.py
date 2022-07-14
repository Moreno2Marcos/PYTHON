# define nomes e salarios
nomes = ['Ana', 'Lucia', 'Maria', 'Paulo']
salarios = [100000, 700000, 900000, 500000]
# iterar e comparar 2 a 2
pos = 0
maxSal = 0
nomMaxSal = None
for salario in salarios:
    if maxSal < salario:
        maxSal = salario
        nomMaxSal = nomes[pos]
    pos = pos + 1
# exibe o maior salario
print('O trabalhador(a) {} recebe o maior salario de R$ {}'.format(nomMaxSal, maxSal))