from datetime import date

# Varíavel de decisão
bissexto = False

# Lê ano
ano = int(input('Digite o ano (0: para ano atual): '))

# Captura o ano atual
if ano == 0:
	ano = date.today().year

# Analisa se o ano é bissexto
if ano % 400 == 0:
	bissexto = True
else:
	if ano % 4 == 0 and ano % 100 != 0:
		bissexto = True

# Imprime se o ano é bissexto
if bissexto == True:
	print(f'O ano {ano} é bissexto')
else:
	print(f'O ano {ano} não é bissexto')