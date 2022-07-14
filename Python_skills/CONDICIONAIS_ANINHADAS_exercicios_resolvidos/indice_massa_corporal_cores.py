# https://www.youtube.com/watch?v=b7r34za963I&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=10

cores = {'del': '\\033[m',
		 'vermelho': '\\033[1;31m',
		 'azul': '\\033[1;34m'}

peso = float(input('Escreva o seu peso em {}(Kg){}: '.format(cores['azul'], cores['del'])))
altura = float(input('Escrea a sua altura em {}(m){}: '.format(cores['azul'], cores['del'])))

imc = peso / pow(altura, 2)  # Cálulo do Índice da Massa Corporal (IMC)

print('O seu status do IMC ({:.1f}), você está '.format(imc), end='')
if imc < 18.5:
	print('{}ABAIXO DO PESO{}'.format(cores['vermelho'], cores['del']))
elif imc <= 25:
	print('no {}PESO IDEAL{}'.format(cores['vermelho'], cores['del']))
elif imc <= 30:
	print('em {}SOBREPESO{}'.format(cores['vermelho'], cores['del']))
elif imc <= 40:
	print('em {}OBESIDADE{}'.format(cores['vermelho'], cores['del']))
else:
	print('em {}OBESIDADE MÓRBIDA{}'.format(cores['vermelho'], cores['del']))