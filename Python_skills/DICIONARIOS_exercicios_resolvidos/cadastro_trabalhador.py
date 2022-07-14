# https://www.youtube.com/watch?v=Vsqemzdrj78&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=25

from datetime import datetime

pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
ano_nasci = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - ano_nasci
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
	pessoa['contratação'] = int(input('Ano de contratação: '))
	pessoa['salário'] = float(input('Salário: R$'))
	anos_contribu = datetime.now().year - pessoa['contratação']
	pessoa['aposentadoria'] = 35 - anos_contribu + pessoa['idade']

print('-=' * 30)
for k, v in pessoa.items():
	print(f'  - {k} tem o valor {v}')