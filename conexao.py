import sqlalchemy as sqla
import pandas as pd
class conexao_banco:
    def __init__(self):
        self.engine = sqla.create_engine('postgresql+psycopg2://renan:rev%40123@postgres.ata:5000/pedidos')
        self.conexao = self.engine.connect()
        self.inspector = sqla.inspect(self.conexao)
    
    def colunas_tabela(self,tabela):
        colunas_table = self.inspector.get_columns(tabela)
        dtype = {}
        for coluna in colunas_table:
            dtype[coluna['name']] = coluna['type']
        return dtype

    def insert_banco(self, dataset:pd.DataFrame):
        dtype = self.colunas_tabela('controle_ordens')        
        dataset.to_sql('controle_ordens',self.engine, if_exists="append",dtype= dtype, index=False)
        