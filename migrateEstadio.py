from cartola.models import Estadio
import pandas as pd

estadiosDF = pd.read_csv('estadios.txt',sep=',',encoding='utf8',header=0,index_col=0)

estadiosDF.apply(lambda x: Estadio.objects.update_or_create(**x),axis=1)
