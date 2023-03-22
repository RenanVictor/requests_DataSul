import tkinter as tk
import atualiza_pedidos as atp

classe_pedidos = atp.pedidos()

#Funções
def get_valores():
    classe_pedidos.pedido.append(int(txtPedidos.get()))
    classe_pedidos.tipo = txtTipo.get()
    classe_pedidos.cria_csv = 'Sim'
    classe_pedidos.data = txtData.get()
    
def btn_implantar():
    get_valores()
    classe_pedidos.atualizar_pedidos()
    classe_pedidos.pedido.clear()

def gerar_csv():
    get_valores()
    classe_pedidos.cria_csv = 'Não'
    classe_pedidos.pedido.clear()


#Recursos Janela
janela = tk.Tk()
janela.title('Localizar pedidos')
tblFrame = tk.Frame(janela)
lblPedidos = tk.Label(tblFrame,text='Nº Pedidos:')
txtPedidos = tk.Entry(tblFrame)
lblTipo = tk.Label(tblFrame,text='Tipo Máq:')
txtTipo = tk.Entry(tblFrame)
lblData = tk.Label(tblFrame,text='Data Pedidos:')
txtData = tk.Entry(tblFrame)
btnImplantar = tk.Button(tblFrame, text='Implantar',command=btn_implantar)
btnGerarCSV = tk.Button(tblFrame, text='Gerar CSV')



# layout janela
tblFrame.grid(row=0, column=0)
lblPedidos.grid(row=0, column= 0, sticky='W' , pady=5)
txtPedidos.grid(row=0,column= 1, sticky='w', padx=5)
lblTipo.grid(row=1, column= 0, sticky='W' , pady=5)
txtTipo.grid(row=1, column= 1, sticky='W' , pady=5)
lblData.grid(row=2, column= 0, sticky='W' , pady=5) 
txtData.grid(row=2, column= 1, sticky='W' , pady=5)
btnImplantar.grid(row=3, column=0, sticky='w', pady=5, padx=10)
btnGerarCSV.grid(row=3, column=1, sticky='w', padx=10)

janela.mainloop()