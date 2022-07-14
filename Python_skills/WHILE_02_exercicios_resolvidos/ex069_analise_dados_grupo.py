# https://www.youtube.com/watch?v=4Ca6iRJo3M0&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=39

tot18 = totalH = totalM20 = 0

print('-'*25)
print('{:^25}'.format('CADASTRE UMA PESSOA'))
print('-'*25)

while True:
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    print('-' * 25)

    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 20:
        totalM20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'S':
        print('-' * 25)
        print('{:^25}'.format('CADASTRE UMA PESSOA'))
        print('-' * 25)
    else:
        break

print('{:=^30}'.format(' FIM DO PROGRAMA '))
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totalH} homens cadastrados')
print(f'E temos {totalM20} mulheres com menos de 20 anos')