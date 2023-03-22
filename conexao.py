import sqlalchemy as sqla
import pandas as pd
import tkinter.messagebox as msx

class conexao_banco:
    def __init__(self):
        self.engine = sqla.create_engine('postgresql+psycopg2://renan:rev%40123@postgres.ata:5000/pedidos')
        self.conexao = self.engine.connect()
        self.inspector = sqla.inspect(self.conexao)
        self.tabela = ''
        self.dataset = pd.DataFrame()
    



    def todas_colunas_tabela(self):
        colunas_table = self.inspector.get_columns(self.tabela)
        dtype = {}
        for coluna in colunas_table:
            dtype[coluna['name']] = coluna['type']
        return dtype

    def se_existe_tabela(self):
        lista_tabelas = self.inspector.get_table_names()
        if self.tabela not in lista_tabelas:
            msx.showwarning(title='Tabela não encontrada!',
            message='A tabela mencionada não foi encontrada, favor informar uma tabela válida!')
            return ''
        else:
            return self.todas_colunas_tabela()

    def colunas_tabela_selecionadas(self,lista_coluna):
        todas_colunas = self.todas_colunas_tabela()
        dtype = {}
        for coluna in lista_coluna:
            dtype[coluna] = todas_colunas[coluna]
        return dtype

    def insert_banco(self):
        dtype = self.se_existe_tabela(self.tabela)        
        self.dataset.to_sql(self.tabela,self.engine, if_exists="append",dtype= dtype, index=False)
        
