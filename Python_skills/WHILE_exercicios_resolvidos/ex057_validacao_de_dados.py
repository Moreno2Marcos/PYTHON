# https://www.youtube.com/watch?v=JGztEBLGj5E&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=26

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]

print('Sexo {} registrado com sucesso'.format(sexo))
