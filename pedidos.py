import pandas as pd
import Request_pedidos
from urllib.parse import urlencode


class create_df_pedidos:
    def __init__(self):
        self.dataset = pd.DataFrame()


    def create_dataframe_pedidos(self):
        self.dataset = pd.DataFrame(Request_pedidos.send_request_pedido().json()['data'])
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
        print(self.dataset[column])

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
        self.converter_ts_datetime('Data_emissao')
        self.converter_ts_datetime('data_entrega')
        #self.dataset.to_csv('Pedidos_Setembro.csv', sep=';', index=False)
        self.create_column_url()

    def eliminando_atendido_total(self):
        self.dataset.query('situacao != ("Atendido Total", "Cancelado")',inplace=True)


    
classe = create_df_pedidos() 


classe.retorna_df_formatado()
classe.dataset.to_csv('Pedidos.csv', sep=';', index=False, encoding="utf-8")