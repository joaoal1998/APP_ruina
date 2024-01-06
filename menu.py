from tkinter import *

#Funções
def nconsulta():
    janela_principal.withdraw()
    import app_rr_simplificado

def sair():
    janela_principal.destroy()

#GUI

janela_principal=Tk()
janela_principal.title('Risco de ruína')
janela_principal.geometry('265x265+550+200')
janela_principal.resizable(True,True)
janela_principal.config(background='#3366cc')

#Widget
logo=PhotoImage(file='imagens/fundo_vazado-removebg-preview.png')
logo=logo.subsample(3,3)
fig1 = Label(image=logo, bg='#3366cc')

bt_nconsulta = Button(janela_principal, text='Nova consulta', bg='#3366cc', 
                      fg='white', bd=0, font=('georgia',15, 'bold'), highlightthickness=0,
                      command=nconsulta)
bt_sair = Button(janela_principal, text='Sair', bg='#3366cc', 
                 fg='white', bd=0, font=('georgia',15, 'bold'), highlightthickness=0,
                 command=sair)

#Layout
fig1.grid(row=0, column=0, padx=(50,0))
bt_nconsulta.grid(row=1, column=0, padx=(50,0))
bt_sair.grid(row=2, column=0, padx=(50,0))

janela_principal.mainloop()