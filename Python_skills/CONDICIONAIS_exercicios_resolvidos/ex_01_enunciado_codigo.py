# fonte do enunciado do problema
# https://www.youtube.com/watch?v=NZiNphKkxhg&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=46

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
	print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')