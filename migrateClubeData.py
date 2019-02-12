import pandas as pd
from cartola.models import *

cluIndexFile = '.\\data\\clubesIndex.csv'
clubeIndex = pd.read_csv(cluIndexFile, sep = ';', header = 0)

clubeIndex['id'] = clubeIndex['ID'].copy()
clubeIndex['nomeCBF'] = clubeIndex['CBF'].copy()
clubeIndex['nome'] = clubeIndex['CART'].copy()
clubeIndex['nomeELO'] = clubeIndex['ELO'].copy()

clubes = []
for ind in clubeIndex.index:
    cRow = clubeIndex.loc[ind,['id','nome','nomeCBF','nomeELO']]
    clubes.append(Clube(**cRow))
