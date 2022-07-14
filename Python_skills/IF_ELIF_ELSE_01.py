# define salarios
salA = 100000  # Manager
salB = 80000  # Executive
salC = 300000  # Asst. Manager	
# comparar os salarios 2 a 2
salMax = 0
title = None
if salA > salB:
    salMax = salA
    title = 'Manager'
else:
    salMax = salB
    title = 'Executive'
if salMax < salC:
    salMax = salC
    title = 'Asst. Manager'
# imprimir a maior salario
print('O {} tem um salário máximo de R$ {} por ano'.format(title, salMax))