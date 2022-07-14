from tkinter import *
from tkinter import messagebox


def function():
	aluno = dict()

	aluno['nome'] = e1.get()
	aluno['média'] = float(e2.get())

	if aluno['média'] >= 7:
		aluno['situação'] = 'Aprovado'
	elif 5 <= aluno['média'] < 7:
		aluno['situação'] = 'Recuperação'
	else:
		aluno['situação'] = 'Reprovado'

	salida = ''
	for k, v in aluno.items():
		salida += f'- {k} é igual a {v}' + '\'

	messagebox.showinfo('Resultados', salida)


root = Tk()

Label(root, text='Nome').grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text='Média').grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)

Button(root, text='Enviar', command=function).grid(row=3, column=1)

root.mainloop()