import pandas as pd
from Request_pedidos import send_request_item
from pedidos import create_df_pedidos as pedidos
import conexao
classe_conexao = conexao.conexao_banco()


class create_df_itens_pedidos:
    def __init__(self):
        self.pedidos = pd.DataFrame()
        self.itens = pd.DataFrame()
        self.pedidos_completo = pd.DataFrame()
        self.funcao = 'Maquinas'
    
    def converte_str_datetime(self,coluna):
        self.pedidos_completo[coluna] = pd.to_datetime(self.pedidos_completo[coluna], format=('%Y/%m/%d'))



    def buscando_df(self):
        self.pedidos = pd.read_csv('Pedidos.csv', sep=';')
    
    def read_csv_pedidos_completo(self):
        self.pedidos_completo = pd.read_csv('Pedidos_completo.csv', sep=';')
        self.converte_str_datetime('dt-entorig')
        self.converte_str_datetime('data_entrega')
        self.converte_str_datetime('Data_emissao')
        
    def buscar_itens(self):
        frames = []
        for url in self.pedidos.url_pedidos:
            dataset_item = pd.DataFrame(send_request_item(url).json()['data'])
            dataset_item['url_pedidos'] = url
            frames.append(dataset_item)
        self.itens = pd.concat(frames)

    def seleciona_colunas(self):
        self.itens = self.itens[['it-codigo','it-codigo-desc','cod-un','cod-refer','qt-pedida','qt-atendida','dt-entorig','nome-abrev',
            'cod-ord-compra','nr-sequencia','nr-pedcli','vl-tot-it','user-impl','cod-sit-item-desc','nat-operacao-desc','url_pedidos']]
        self.itens['dt-entorig'] = self.itens['dt-entorig'] /1000
        self.itens['dt-entorig'] = pd.to_datetime(self.itens['dt-entorig'],unit='s')
        self.itens['dt-entorig'] = pd.to_datetime(self.itens['dt-entorig'].dt.strftime('%Y/%m/%d'))
    
    def merge_tabelas(self):
        self.pedidos_completo = pd.merge(self.itens, self.pedidos, on='url_pedidos', how='left')
        self.pedidos_completo.drop(columns=['cod-ord-compra','url_pedidos','nat-operacao-desc','Vendedor','Cliente','n_ped_cliente'], inplace=True)
        self.pedidos_completo.to_csv('Pedidos_completo.csv', sep=';', index=False,encoding="utf-8-sig")
    
    def buscando_por_pedidos(self,pedidos):
        self.pedidos = self.pedidos[self.pedidos.n_pedido.isin(pedidos)]

    def gera_tabela_pedidos(self,data:str):#data deve ser dd/mm/yyyy
        classe_pedidos = pedidos()
        classe_pedidos.data_pedidos = data
        classe_pedidos.retorna_df_formatado()
        #classe_pedidos.eliminando_atendido_total()
        self.pedidos = classe_pedidos.dataset

# Inserindo no banco
    def create_lista_colunas(self):
        if self.funcao == 'Maquinas':
            lista_colunas = ['cliente','pedido','item','referencia','descricao','qtd','entrega','emissao','tipo']        
            classe_conexao.dataset = self.pedidos_completo[['nome-abrev','n_pedido','it-codigo','cod-refer','it-codigo-desc','qt-pedida','data_entrega','Data_emissao']]
        else:
            import datetime
            lista_colunas = ['op_maq','item','descricao','qtd','referencia','emissao','pedido','entrega','cliente','tipo']
            classe_conexao.dataset = self.pedidos_completo[['ordem','codigo','descricao','qtd_ord','referencia','data_inicio','pedido','data_fim']]
            classe_conexao.dataset['cliente'] = 'ESTOQUE'
            classe_conexao.dataset['pedido'] = 99999
        return lista_colunas

    def teste_df_ordem(self):
        return classe_conexao.dataset
    
    def add_pedidos_tabela(self,tipo):
        classe_conexao.tabela = 'pedidos'
        colunas = self.create_lista_colunas()
        dtype = classe_conexao.colunas_tabela_selecionadas(colunas)
        classe_conexao.dataset['tipo'] = tipo
        classe_conexao.dataset.columns = colunas
        classe_conexao.dataset.to_sql(classe_conexao.tabela,classe_conexao.engine, if_exists="append",dtype= dtype, index=False)

