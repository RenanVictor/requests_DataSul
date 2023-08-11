import pandas as pd
import Request_ordens
from numpy import nan
import conexao

class create_df_ordens:
    def __init__(self):
        self.dataset = pd.DataFrame()
        self.data_api = Request_ordens.dic_data_api()
        self.estado = pd.DataFrame({'numero':[1,2,3,4,5,6,7,8],
            'nome':['Não Iniciada','Liberada','Reservada','Separada','Requisitada','Iniciada','Finalizada','Terminada'],
            'coluna':['statusNotStart','statusReleased','statusReserved','statusKitted','statusIssued','statusStarted','Não Definido','Não Definido']})

# Envio do request e criação do dataframe de acordo com as ordens
    def create_dataframe_from_json(self, response_json):
        dataset_resultado = pd.DataFrame(
            response_json.json()['data']['ttOrdProdVO'])
        print(response_json)
        return dataset_resultado

    def cria_faixa_ordem(self, op_ininial, op_final):
        frames = []
        while (op_ininial <= op_final):
            self.data_api['ttAppointmentParam']['prodOrderCodeIni'] = op_ininial
            op_ininial = op_ininial+50
            self.data_api['ttAppointmentParam']['prodOrderCodeFin'] = op_ininial
            dataset_faixa = self.create_dataframe_from_json(
                Request_ordens.send_request(self.data_api))
            print(str(len(dataset_faixa)) + '_______' + str(op_ininial))
            frames.append(dataset_faixa)
        self.dataset = pd.concat(frames)
        return self.dataset

    def retorna_df_por_ordem(self,ordem):
        self.data_api['ttAppointmentParam']['prodOrderCodeIni'] = ordem
        self.data_api['ttAppointmentParam']['prodOrderCodeFin'] = ordem
        self.dataset = self.create_dataframe_from_json(Request_ordens.send_request(self.data_api))
        return self.dataset
    


    def retorna_df_por_codigo(self,codigo):
        self.data_api['ttAppointmentParam']['itemCodeIni'] = codigo
        self.data_api['ttAppointmentParam']['itemCodeFin'] = codigo
        self.dataset = self.create_dataframe_from_json(Request_ordens.send_request(self.data_api))
        return self.dataset

    def retorna_estado(self,string):
        for item in self.estado.index:
            if self.estado.loc[item,'coluna']!= 'Não Definido':
                if self.estado.loc[item,'nome'] == string:
                    self.data_api['ttAppointmentParam'][self.estado.loc[item,'coluna']] = 'true'
                else:
                    self.data_api['ttAppointmentParam'][self.estado.loc[item,'coluna']] = 'false'

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

    def lista_estado(self):# usar o recurso map do pandas
        lista = []
        for item in self.dataset['statusType']:
            lista.append(self.estado.iloc[(self.estado.index[self.estado['numero']==item][0])][1])
        self.dataset['estado_ordem'] = lista

    def tratamento_dos_dados(self):
        self.dataset.drop(columns=['productionOrderString', 
                                   'qtdPreview', 'machineGroup', 'progressOrder', 
                                   'referDescription', 'balanceTimeSetup', 'balanceTimeActivity', 
                                   'opCode', 'logSfc', 'siteCode', 'machineCode', 'opSfcCode', 
                                   'qtdScrap', 'splitCode'], inplace=True)
        self.dataset[['endDate', 'iniDate']] = self.dataset[['endDate', 'iniDate']].astype(str)
        self.insert_string_time('iniDate')
        self.insert_string_time('endDate')
        self.lista_estado()
        self.dataset.drop(columns=['statusType', 'prtProd', 'prtProd', 'customer'], inplace=True)

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
    df.to_csv('ordens.csv', index=False, sep=';', encoding='utf-8-sig')


#classe_ordem = create_df_ordens()
#bd_conexao = conexao.conexao_banco()


#classe = create_df_ordens()
#dataset = classe.retorna_df_por_ordem(532041)

#print(dataset)
# gerar_csv(dataset)

'''classe_ordem.dataset = pd.read_csv('ordens.csv', sep=';')
classe_ordem.tratamento_dos_dados()
classe_ordem.ordenando_colunas()
classe_ordem.alterar_linhas_vazias()
'''
#bd_conexao.insert_banco(classe_ordem.dataset)
#gerar_csv(classe_ordem.dataset)
