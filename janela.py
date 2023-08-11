import tkinter as tk
import atualiza_pedidos as atp
from tkinter import ttk
import time
import ordens
import pandas as pd

#https://www.pythontutorial.net/tkinter/tkinter-grid/

classe_pedidos = atp.pedidos()
classe_ordens = ordens.create_df_ordens()

#Funções Gerais
def lista_pedidos(string):
    #string = txtPedidos.get()
    lista = string.split(sep=',')
    lista_int = [int(i) for i in lista]
    return lista_int

def update_progress(valor):
    pb['value'] += valor
    #time.sleep(1)


#Funções Pedidos
def verifica_pedidos():
    update_progress(20)
    if ',' in txtPedidos.get():
        classe_pedidos.pedido  = lista_pedidos(txtPedidos.get())
    else:
        classe_pedidos.pedido.append(int(txtPedidos.get()))

def get_valores():
    verifica_pedidos()
    update_progress(20)
    classe_pedidos.tipo = txtTipo.get()
    classe_pedidos.cria_csv = 'Sim'
    classe_pedidos.data = txtData.get()
    
def btn_implantar():
    get_valores()
    update_progress(20)
    classe_pedidos.atualizar_pedidos()
    classe_pedidos.pedido.clear()

def gerar_csv():
    get_valores()
    update_progress(20)
    classe_pedidos.cria_csv = 'Não'
    classe_pedidos.atualizar_pedidos()
    classe_pedidos.pedido.clear()

#Funções ordens Componentes
def verificar_ordens():
    if ',' in txtOrdens.get():
        lista_ordens = lista_pedidos(txtOrdens.get())
        frames = []
        for ordem in lista_ordens:
            dataset_ordem = classe_ordens.retorna_df_por_ordem(ordem)
            frames.append(dataset_ordem)
        classe_ordens.dataset = pd.concat(frames)
    else:
        classe_ordens.dataset = classe_ordens.retorna_df_por_ordem(txtOrdens.get())
    classe_ordens.tratamento_dos_dados()
    classe_ordens.ordenando_colunas()
    return classe_ordens.dataset

def valores_ordens():
    classe_pedidos.tipo = txtTipo.get()
    classe_pedidos.atualiza_ordens(verificar_ordens())

def btnComponentes():
    valores_ordens()


#Recursos Janela
janela = tk.Tk()
janela.title('Localizar pedidos')
tblFrame = tk.Frame(janela)
tblbutton = tk.Frame(janela)
lblPedidos = tk.Label(tblFrame,text='Nº Pedidos:')
txtPedidos = tk.Entry(tblFrame)
lblOrdens = tk.Label(tblFrame,text='Nº Ordens:')
txtOrdens = tk.Entry(tblFrame)
lblTipo = tk.Label(tblFrame,text='Tipo Máq:')
txtTipo = tk.Entry(tblFrame)
lblData = tk.Label(tblFrame,text='Data Pedidos:')
txtData = tk.Entry(tblFrame)
btnImplantar = tk.Button(tblFrame, text='Implantar',command= btn_implantar)
btnGerarCSV = tk.Button(tblFrame, text='Gerar CSV', command= gerar_csv)
btnComp = tk.Button(tblFrame,text='Add Comp.',command= btnComponentes)
pb = ttk.Progressbar(janela,orient= 'horizontal',mode= 'determinate')




# layout janela
tblFrame.grid(row=0, column=0)
#tblbutton.grid(row=1, column=0)
lblPedidos.grid(row=0, column= 0, sticky='W', pady=5)
txtPedidos.grid(row=0,column= 1, sticky='Ew', padx=5, columnspan=2)
lblOrdens.grid(row=1, column= 0, sticky='W', pady=5)
txtOrdens.grid(row=1,column= 1, sticky='Ew', padx=5, columnspan=2)
lblTipo.grid(row=2, column= 0, sticky='W', pady=5)
txtTipo.grid(row=2, column= 1, sticky='EW', pady=5, padx=5, columnspan=2)
lblData.grid(row=3, column= 0, sticky='W', pady=5) 
txtData.grid(row=3, column= 1, sticky='EW', pady=5, padx=5, columnspan=2)
btnImplantar.grid(row=4, column=0, sticky='w', pady=5, padx=10)
btnGerarCSV.grid(row=4, column=1, sticky='w', padx=10)
btnComp.grid(row=4, column=2, sticky='w', padx=10)
pb.grid(column=0,row=5,columnspan=3,padx=10,pady=10,sticky='EW')

janela.mainloop()