import pandas as pd
from Request_pedidos import send_request_item
from pedidos import create_df_pedidos as pedidos

class create_df_itens_pedidos:
    def __init__(self):
        self.pedidos = pd.DataFrame()
        self.itens = pd.DataFrame()
        self.pedidos_completo = pd.DataFrame()
    
    def buscando_df(self):
        self.pedidos = pd.read_csv('Pedidos.csv', sep=';')
    

    def converte_str_in_datetime(self):
        self.pedidos['Data_emissao'] = pd.to_datetime(self.pedidos['Data_emissao'])
        self.pedidos['data_entrega'] = pd.to_datetime(self.pedidos['data_entrega'])
        
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
        self.pedidos_completo.to_csv('Pedidos_completo.csv', sep=';', index=False,encoding="utf-8")
    


classe_pedidos = pedidos()
classe_itens = create_df_itens_pedidos()

classe_pedidos.retorna_df_formatado()

classe_itens.pedidos = classe_pedidos.dataset
classe_itens.buscar_itens()
classe_itens.seleciona_colunas()
classe_itens.merge_tabelas()

