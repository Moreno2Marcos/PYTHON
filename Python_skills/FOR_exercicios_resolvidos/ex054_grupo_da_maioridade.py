# https://www.youtube.com/watch?v=IL5iBWoKRIs&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=22

from datetime import date

ano_atual = date.today().year

tot_menor = 0
tot_maior = 0

for c in range(0, 7):
    ano_nasc_pess = int(input('Em que ano a {}ª de nascimento? '.format(c+1)))
    idade = ano_atual - ano_nasc_pess
    if idade >= 21:
        tot_maior = tot_maior + 1
    else:
        tot_menor = tot_menor + 1

print("\nAo todo tivemos {} pessoas maoires de idade".format(tot_maior))
print('E também tivemos {} pessoas menores de idade'.format(tot_menor))
