from datetime import date

cores = {'del': '\\033[m',
		 'azul': '\\033[1;34m'}

ano_atual = date.today().year

ano_nasc = int(input('Escreva ano de nascimento do atleta: '))

idade = ano_atual - ano_nasc

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
	print('Classificação: {}MIRIM{}'.format(cores['azul'], cores['del']))
elif idade <= 14:
	print('Classificação: {}INFANTIL{}'.format(cores['azul'], cores['del']))
elif idade <= 19:
	print('Classificação: {}JUNIOR{}'.format(cores['azul'], cores['del']))
elif idade <= 25:
	print('Classificação: {}SÊNIOR{}'.format(cores['azul'], cores['del']))
else:
	print('Classificação: {}MASTER{}'.format(cores['azul'], cores['del']))