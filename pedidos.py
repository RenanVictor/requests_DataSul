import pandas as pd
import Request_pedidos
from urllib.parse import urlencode


class create_df_pedidos:
    def __init__(self):
        self.dataset = pd.DataFrame()
        self.data_pedidos = ''


    def create_dataframe_pedidos(self):
        self.dataset = pd.DataFrame(Request_pedidos.send_request_pedido(self.data_pedidos).json()['data'])
        #self.dataset.style.set_properties(**{'text-align': 'left'})
        return self.dataset

    def selecionando_colunas(self):
        self.dataset = self.dataset[['orderAdder','dt-emissao','nr-pedido','nome-abrev',
            'dt-entrega','cod-sit-ped-desc','nr-pedcli']]
        lista_colunas = ['Vendedor','Data_emissao','n_pedido','Cliente','data_entrega','situacao','n_ped_cliente']
        self.dataset.columns = lista_colunas

    def converter_ts_datetime(self, column):
        self.dataset[column] = self.dataset[column] /1000
        self.dataset[column] = pd.to_datetime(self.dataset[column],unit='s')
        self.dataset[column] = pd.to_datetime(self.dataset[column].dt.strftime('%Y/%m/%d'))
        #print(self.dataset[column])

    def create_column_url(self):# retorna uma lista caso o usuário necessite apenas dos url's
        lista_url = []
        for item in self.dataset[['n_ped_cliente','Cliente']].values:
            parametro = {'customer_order':item[0],'short_name':item[1]}
            lista_url.append(urlencode(parametro, doseq=True))
        self.dataset['url_pedidos'] = lista_url
        return lista_url

    def retorna_df_formatado(self):
        self.create_dataframe_pedidos()
        self.selecionando_colunas()
        self.dataset.query('n_pedido != 48115 and n_pedido !=49112',inplace=True)# Pedido com data inválida no mês 03/2023 e 06/2023
        self.converter_ts_datetime('Data_emissao')
        self.converter_ts_datetime('data_entrega')
        self.create_column_url()

    def eliminando_atendido_total(self):
        self.dataset.query('situacao != ("Atendido Total", "Cancelado")',inplace=True)
