# https://www.youtube.com/watch?v=EQQt-6QqXOs&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=32

nome = str(input('Digite seu nome completo: ')).strip()

print('Em maiúsculas: {}'.format(nome.upper()))
print('Em minúsculas: {}'.format(nome.lower()))
print('Seu primeiro nome é: {}'.format(nome.split()[0]))
print('Número de letras ao todo sem espaços: {}'.format(len(nome) - nome.count(' ')))

print('Número de letras do seu primeiro nome: {} letras'.format(len(nome.split()[0])))
print('Número de letras do seu primeiro nome: {} letras'.format(nome.find(' ')))  # cuidado!
