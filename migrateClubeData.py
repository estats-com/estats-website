import pandas as pd
from cartola.models import *
from django.core.files import File

cluIndexFile = '.\\data\\clubesIndex.csv'
clubeIndex = pd.read_csv(cluIndexFile, sep = ';', header = 0)

clubeIndex['cartola_id'] = clubeIndex['ID'].copy()
clubeIndex['nomeCBF'] = clubeIndex['CBF'].copy()
clubeIndex['nome'] = clubeIndex['CART'].copy()
clubeIndex['nomeELO'] = clubeIndex['ELO'].copy()

clubes = []
for ind in clubeIndex.index:
    cRow = clubeIndex.loc[ind,['cartola_id','nome','nomeCBF','nomeELO']]
    clu = Clube(**cRow)
    try:
        clu.escudoP.save('%s.png'%clu.cartola_id,
                     File(open('pequeno/%s.png'%clu.cartola_id, 'rb')))
        clu.escudoM.save('%s.png'%clu.cartola_id,
                     File(open('C:/users/Juan/Dropbox/cartola/escudo/medio/%s.png'%clu.cartola_id, 'rb')))
        clu.escudoG.save('%s.png'%clu.cartola_id,
                     File(open('C:/users/Juan/Dropbox/cartola/escudo/grande/%s.png'%clu.cartola_id, 'rb')))
    except:
        pass
    clu.save()
