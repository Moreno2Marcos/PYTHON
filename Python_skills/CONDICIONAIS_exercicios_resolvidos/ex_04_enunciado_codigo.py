# https://www.youtube.com/watch?v=PGqHyzWoagc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=42

distancia = float(input('Qual é a distância da sua viagem? '))

print('Você está prestes a começar uma viagem de {} Km.'.format(distancia))

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('E o preço da sua passagem será de R$ {:.2f}'.format(preco))