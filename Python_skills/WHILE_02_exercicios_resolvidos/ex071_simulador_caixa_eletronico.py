# https://www.youtube.com/watch?v=_XGgwltYpYk&list=PLHz_AreHm4dk_nZHmxxf_J0WRAqy5Czye&index=41

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)

valor = int(input('Que valor quer sacar? R$'))
total = valor

cedula = 50
totalCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalCedula = 0  # cada vez que mude a nota
        if total == 0:  # se o dinheiro acabar!
            break

print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
