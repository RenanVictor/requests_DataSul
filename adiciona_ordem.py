import pandas as pd
import ordens as op
import psycopg2 as psy

classe = op.create_df_ordens()

lista_ordens = [1289537,1289609,1289610,1289611,1289781,1289914,1289915]


def ordens_lista(lista):
    frames = []
    for ordem in lista:
        dataset_ordem = classe.retorna_df_por_ordem(int(ordem))
        frames.append(dataset_ordem)
    dataset_ordens = pd.concat(frames)
    return dataset_ordens

def tratamento(dataset):
    classe.dataset = dataset
    classe.tratamento_dos_dados()
    classe.ordenando_colunas()
    classe.alterar_linhas_vazias()

