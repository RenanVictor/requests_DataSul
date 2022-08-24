import pandas as pd
import Request_ordens
from numpy import nan
import conexao

class create_df_ordens:
    def __init__(self):
        self.dataset = pd.DataFrame()
        self.data_api = Request_ordens.dic_data_api()

# Envio do request e criação do dataframe de acordo com as ordens
    def create_dataframe_from_json(self, response_json):
        dataset_resultado = pd.DataFrame(
            response_json.json()['data']['ttOrdProdVO'])
        return dataset_resultado

    def cria_faixa_ordem(self, op_ininial, op_final):
        frames = []
        while (op_ininial <= op_final):
            self.data_api['ttAppointmentParam']['prodOrderCodeIni'] = op_ininial
            op_ininial = op_ininial+50
            self.data_api['ttAppointmentParam']['prodOrderCodeFin'] = op_ininial
            dataset_faixa = self.create_dataframe_from_json(
                Request_ordens.send_request(self.data_api))
            print(len(dataset_faixa) + '_______' + op_ininial)
            frames.append(dataset_faixa)
            self.dataset = pd.concat(frames)
        return self.dataset
    
    def retorna_df_por_codigo(self,codigo):
        self.data_api['ttAppointmentParam']['itemCodeIni'] = codigo
        self.data_api['ttAppointmentParam']['itemCodeFin'] = codigo
        return

# Tratamento e organização dos dados do dataframe

    def insert_string_time(self, string):
        lista = []
        for item in self.dataset[string]:
            if len(item) == 8:
                lista.append(str(item[0:2]+'/' + item[2:4] + '/' + item[4:]))
            else:
                lista.append(str(item[0]+'/' + item[1:3] + '/' + item[3:]))
        self.dataset[string] = lista
        self.dataset[string] = pd.to_datetime(
            self.dataset[string], format='%d/%m/%Y')

    def lista_estado(self):
        lista = []
        for item in self.dataset['statusType']:
            if item == 1:
                lista.append('Não Iniciada')
            elif item == 2:
                lista.append('Liberada')
            elif item == 3:
                lista.append('Reservada')
            elif item == 4:
                lista.append('Separada')
            elif item == 5:
                lista.append('Requisitada')
            elif item == 6:
                lista.append('Iniciada')
            elif item == 7:
                lista.append('Finalizada')
            elif item == 8:
                lista.append('Terminada')
            else:
                lista.append('Não Definido')
        self.dataset['estado_ordem'] = lista

    def tratamento_dos_dados(self):
        self.dataset.drop(columns=['productionOrderString', 
                                   'qtdPreview', 'machineGroup', 'progressOrder', 
                                   'referDescription', 'balanceTimeSetup', 'balanceTimeActivity', 
                                   'opCode', 'logSfc', 'siteCode', 'machineCode', 'opSfcCode', 
                                   'qtdScrap', 'splitCode'], inplace=True)
        self.dataset[['endDate', 'iniDate']] = self.dataset[[
            'endDate', 'iniDate']].astype(str)
        self.insert_string_time('iniDate')
        self.insert_string_time('endDate')
        self.lista_estado()
        self.dataset.drop(
            columns=['statusType', 'prtProd', 'prtProd', 'customer'], inplace=True)

# Preparação dos dados para enviar para o banco de dados
    def ordenando_colunas(self):  # melhorar esta função caso mude as colunas
        colunas = self.dataset.columns.tolist()
        colunas_ordenadas = []
        colunas_ordenadas.append(colunas[5])
        colunas_ordenadas.append(colunas[1])
        colunas_ordenadas.append(colunas[4])
        colunas_ordenadas.append(colunas[7])
        colunas_ordenadas.append(colunas[3])
        colunas_ordenadas.append(colunas[2])
        colunas_ordenadas.append(colunas[10])
        colunas_ordenadas.append(colunas[9])
        colunas_ordenadas.append(colunas[0])
        colunas_ordenadas.append(colunas[6])
        colunas_ordenadas.append(colunas[8])
        self.dataset = self.dataset[colunas_ordenadas]
        self.dataset.columns = ["ordem", "codigo", "descricao", "qtd_ord", "planejador",
                                "referencia", "estado", "data_inicio", "data_fim", "qtd_prod", "pedido"]

    def alterar_linhas_vazias(self):
        self.dataset['pedido'] = self.dataset['pedido'].fillna(0).astype(int)
        self.dataset['referencia'].replace(nan, '', inplace=True)



def gerar_csv(df: pd.DataFrame):
    df.to_csv('dataset_ordens_plan1.csv', index=False, sep=';')


classe_ordem = create_df_ordens()
#dataset = classe_ordem.cria_faixa_ordem(1273471,1306668)
# print(dataset)
# gerar_csv(dataset)

classe_ordem.dataset = pd.read_csv('dataset_ordens_plan.csv', sep=';')
classe_ordem.tratamento_dos_dados()
classe_ordem.ordenando_colunas()
classe_ordem.alterar_linhas_vazias()

bd_conexao = conexao.conexao_banco()


#bd_conexao.insert_banco(classe_ordem.dataset)
#gerar_csv(classe_ordem.dataset)
