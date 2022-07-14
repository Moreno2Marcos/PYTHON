# https://www.youtube.com/watch?v=IV13X0QOMU8&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=3

casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = (casa / anos) / 12
minimo = salario * 30 / 100

print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, anos), end=' ')
print('a prestação será de R$ {:.2f}'.format(prestacao))

if prestacao <= minimo:
	print('Empréstimo poder ser CONCEDIDO!')
else:
	print('Empréstimo NEGADO!')