# https://www.youtube.com/watch?v=SifYYsXhLM8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=37

nome = str(input('Escreva o seu nome completo: ')).strip()

nome = nome.split()

print('Primeiro: {}\nÚltimo: {}'.format(nome[0], nome[len(nome)-1]))
