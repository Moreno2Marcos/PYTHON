cores = {'del': '\\033[m',
		 'vermelho': '\\033[1;31m'}

n1 = float(input('Escreva a primeira nota do aluno: '))
n2 = float(input('Escreva a segunda nota do aluno: '))

media = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, media))

if media < 5:
	print('{}O aluno está REPROVADO{}'.format(cores['vermelho'], cores['del']))
elif 5 <= media < 7:  # media >= 5.0 and media < 7.0
	print('{}O aluno está em RECUPERAÇÃO{}'.format(cores['vermelho'], cores['del']))
elif media >= 7:
	print('{}O aluno está APROVADO{}'.format(cores['vermelho'], cores['del']))