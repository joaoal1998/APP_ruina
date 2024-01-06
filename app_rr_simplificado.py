from tkinter import *
from tkinter import messagebox
import math as m
import sys
import os

#Funções
def calcular():

    if ent_acerto.get()== '' or ent_derrotas.get()== '' or ent_eventos.get()== '' or ent_montante.get()== '' or ent_payoff.get()== '':
        messagebox.showerror('Erro','Preencha todos os campos!')
        return
    try:
        capital_inicial = float(ent_montante.get())
        taxa_acerto = float(ent_acerto.get())/100
        payoff = float(ent_payoff.get())
        eventos = int(ent_eventos.get())
        derrotas = int(ent_derrotas.get())
        taxa_erro = (1 - taxa_acerto)
        vitorias = eventos - derrotas
        c = m.factorial(eventos) / (m.factorial(derrotas) * m.factorial(eventos - derrotas))
        p = c * (taxa_erro ** derrotas) * (taxa_acerto ** vitorias)
        parte = capital_inicial / eventos
        saldo = parte * payoff * vitorias - parte * derrotas

        messagebox.showinfo('Resultado',f'Você tem {round(p*100,2)}% de chance de errar {derrotas} jogadas aleatórias dos '
                            f'{eventos} eventos especificados. Nesse cenário, seu retorno seria de '
                            f'{round(saldo/capital_inicial*100,2)}% e o seu saldo acumulado seria '
                            f'R${capital_inicial+saldo}')
        
        '''txt_result['text'] =(f'Você tem {round(p*100,2)}% de chance de errar \n{derrotas} jogadas aleatórias dos '
                            f'{eventos} eventos especificados\nNesse cenário,seu retorno seria de '
                            f'{round(saldo/capital_inicial*100,2)}% e o seu saldo acumulado seria '
                            f'R${capital_inicial+saldo}')'''
    except ValueError:
        messagebox.showerror('erro','Insira apenas valores numéricos! Para número decimal, utilize ponto(.) como separador.')
        
def sair():
    janela_principal.destroy()

def fecha_e_reinicia():
    janela_principal.destroy()
    menu = sys.executable
    os.execl(menu, menu, * sys.argv)

#GUI
cor='#3366cc'
janela_principal=Tk()
janela_principal.title('Consulta')
janela_principal.geometry('450x210+550+200')
janela_principal.resizable(True,True)
janela_principal.config(background=cor)

#Widget
title_rr = Label(janela_principal,text='Calcular risco de ruína',
                 font=('georgia',18), bg=cor, fg='white')

txt_montante = Label(janela_principal, text = 'Montante: ', bg=cor, fg='white', font=('georgia', 10,))
ent_montante = Entry(janela_principal)

txt_acerto = Label(janela_principal, text = 'Taxa de acerto: ', bg=cor, fg='white', font=('georgia', 10,))
ent_acerto = Entry(janela_principal)

txt_payoff = Label(janela_principal, text = 'Payoff: ', bg=cor, fg='white', font=('georgia', 10,))
ent_payoff = Entry(janela_principal)

txt_eventos = Label(janela_principal, text = 'Eventos: ', bg=cor, fg='white', font=('georgia', 10,))
ent_eventos = Entry(janela_principal)

txt_derrotas = Label(janela_principal, text = 'Número de derrotas: ', bg=cor, fg='white', font=('georgia', 10,))
ent_derrotas = Entry(janela_principal)

bt_calcular = Button(janela_principal, text='calcular', command=calcular, font=('georgia', 15, 'bold'),
                      bg=cor, fg='white', highlightthickness=0, bd=0)
bt_sair = Button(janela_principal, text='Sair', command=sair, font=('georgia', 15, 'bold'), 
                      bg=cor ,fg='white', highlightthickness=0, bd=0)

volta = PhotoImage(file='imagens/5649483-removebg-preview (1).png', master=janela_principal)
volta = volta.subsample(10,10)
fig2 = Label(janela_principal, image=volta)
fig2.image = volta

bt_fecha_e_reinicia = Button(janela_principal, image=volta, command=fecha_e_reinicia, bg=cor, highlightthickness=0, bd=0)

#txt_result = Label(janela_principal, text='', bg=cor, font=('georgia', 10))

#Layout
title_rr.grid(row = 0, column=0, padx=(20,0),pady=(0,0))

txt_montante.grid(row=1 , column=0, padx=(20,0))
ent_montante.grid(row=1 , column=1)

txt_acerto.grid(row=2 , column=0, padx=(20,0))
ent_acerto.grid(row=2 , column=1)

txt_payoff.grid(row=3 , column=0, padx=(20,0))
ent_payoff.grid(row=3 , column=1)

txt_eventos.grid(row=4 , column=0, padx=(20,0))
ent_eventos.grid(row=4 , column=1)

txt_derrotas.grid(row=5 , column=0, padx=(20,0))
ent_derrotas.grid(row=5 , column=1)

bt_calcular.grid(row=7 , column=0, padx=(20,0), ipadx=20, ipady=5)
bt_sair.grid(row=7 , column=1, ipadx=10, ipady=5)
bt_fecha_e_reinicia.grid(row=0, column=1, padx=(60,0))

#txt_result.grid(row=8, column=0, columnspan=2, sticky=W+E, padx=(20,0) )

janela_principal.mainloop()