# https://www.youtube.com/watch?v=fokDF4th0IY&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=24

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
cont_M_menos_20 = 0

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma_idade += idade

    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo in 'Ff' and idade < 20:
        cont_M_menos_20 += 1

media_idade = soma_idade / 4

print('\nA média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_homem_mais_velho ))
print('Ao todo são {} mulheres com menos de 20 anos'.format(cont_M_menos_20))