# Calcute the factorial of a number
number = int(input('Digite um número para\ncalcular seu fatorial: '))
# Variable to accumulate the result
fact = 1
print('Calculando {}! = '.format(number), end='')
# Backward approach
for cont in range(number, 0, -1):
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    # Update the accumulative variable
    fact *= cont
print('{}'.format(fact))