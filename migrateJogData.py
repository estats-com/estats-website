import pandas as pd
from cartola.models import *

ano = 2018
scoutsFile = '.\\data\\%s\\scouts.csv'%ano
scouts = pd.read_csv(scoutsFile, sep = ';', decimal=',',header = 0, index_col=[0,1])

jogsInd = scouts.index.get_level_values(0).unique()

jogs = scouts.loc[~scouts.index.get_level_values(0).duplicated()]

jogs = jogs.reset_index()[['ID','NOME','POSICAO']]
jogs.columns = map(lambda x: x.lower(), jogs.columns)
jogs['cartola_id'] = jogs.id.copy()
jogsObj = jogs[['cartola_id','nome','posicao']].apply(lambda x: Jogador.objects.update_or_create(**x), axis = 1)
