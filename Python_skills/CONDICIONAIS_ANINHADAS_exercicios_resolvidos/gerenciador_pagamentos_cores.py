# https://www.youtube.com/watch?v=I-SH3QchuZ4&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=11

# Estabelece as cores usadas no programa
cores = {'del': '\\033[m',
		 'azul': '\\033[1;34m',
		 'pretoebranco': '\\033[7;30m',
		 'branco': '\\033[1;30m'}

# Imprime Tabela de opções
print('\{}Tabela de condições de pagamento{}'.format(cores['branco'], cores['del']))
print('{}-{}'.format(cores['branco'], cores['del']) * 32)
print(' ' * 6 + '{}1 - {}{}à vista dinheiro/cheque{}'.format(cores['branco'], cores['del'], cores['azul'],
															 cores['del']))
print(' ' * 6 + '{}2 - {}{}à vista no cartão{}'.format(cores['branco'], cores['del'], cores['azul'], cores['del']))
print(' ' * 6 + '{}3 - {}{}em até 2x no cartão{}'.format(cores['branco'], cores['del'], cores['azul'], cores['del']))
print(' ' * 6 + '{}4 - {}{}3x ou mais no cartão{}'.format(cores['branco'], cores['del'], cores['azul'], cores['del']))
print('{}-{}'.format(cores['branco'], cores['del']) * 32 + '\')

# Entrada de dados
preco_normal = float(input('Escreva o preço das compras: R$'))
opcao = int(input('Quel é a opção da Tabela acima mostrada? '))

# Calcula e mostra o preço final do produto a ser pago

if opcao == 1:
	total = preco_normal - 0.1 * preco_normal
elif opcao == 2:
	total = preco_normal - 0.05 * preco_normal
elif opcao == 3:
	total = preco_normal
	parcela = total / 2
	print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(parcela))
elif opcao == 4:
	total = preco_normal + 0.2 * preco_normal
	total_parc = int(input('Quantas parcelas? '))
	parcela = total / total_parc
	print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(total_parc, parcela))
else:
	total = -1

if total == -1:
	print('\\033[1;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\\033[m')
else:
	print('Sua compra de R${} vai custar {}R${:.2f}{} no final'.format(preco_normal, cores['pretoebranco'], total,
																   cores['del']))
]