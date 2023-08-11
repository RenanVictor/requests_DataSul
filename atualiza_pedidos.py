import itens_pedidos as itp

classe = itp.create_df_itens_pedidos()

class pedidos:
    def __init__(self):        
        self.pedido = []
        self.tipo = ''
        self.cria_csv = 'Sim'
        self.data = ''
        
    def gerar_itens_pedidos_completo(self):
        classe.buscar_itens()
        classe.seleciona_colunas()
        classe.merge_tabelas()

    def atualizar_pedidos(self):
        classe.gera_tabela_pedidos(self.data)
        classe.buscando_por_pedidos(self.pedido)
        self.gerar_itens_pedidos_completo()
        if self.cria_csv =='Sim':
            classe.add_pedidos_tabela(self.tipo)

    def atualiza_ordens(self,dataset):
        classe.funcao = 'Componentes'
        classe.pedidos_completo = dataset
        #classe.teste_df_ordem()
        classe.add_pedidos_tabela(self.tipo)



'''classe_pedidos = pedidos()
classe_pedidos.cria_csv = 'Não'
classe_pedidos.pedido = [48513]
classe_pedidos.atualizar_pedidos()'''
