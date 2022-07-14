numero = int(input('\\033[35mDigite um número qualquer: \\033[m'))

resultado = numero % 2

if resultado == 0:
	print('O número {} é \\033[34mPAR\\033[m'.format(numero))
else:
	print('O número {} é \\033[34mÍMPAR\\033[m'.format(numero))