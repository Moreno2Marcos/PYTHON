cores = {'del': '\\033[m',
		 'magenta': '\\033[1;35m',
		 'vermelho': '\\033[1;31m'}

l1 = float(input('Escreva o comprimento do primeiro lado do triângulo: '))
l2 = float(input('Escreva o comprimento do segundo lado do triângulo: '))
l3 = float(input('Escreva o comprimento do terceiro lado do triângulo: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
	print('Os lados digitados {}PODEM{} formar um triângulo'.format(cores['vermelho'], cores['del']), end=' ')
	if l1 == l2 == l3:  # l1 == l2 and l2 == l3
		print('{}EQUILÁTERO{}'.format(cores['magenta'], cores['del']))
	elif l1 == l2 or l1 == l3 or l2 == l3:
		print('{}ISÓSCELES{}'.format(cores['magenta'], cores['del']))
	else:
		print('{}ESCALENO{}'.format(cores['magenta'], cores['del']))
else:
	print('Os lados digitados {}NÃO PODEM{} forma um triângulo!'.format(cores['vermelho'], cores['del']))