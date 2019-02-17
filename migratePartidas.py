# -*- coding: utf-8 -*-
import pandas as pd
from cartola.models import Partida, Estadio, Clube
from django.utils import timezone

ano = 2018
repo = ("C:/users/Juan/Dropbox/"
       "Cartola/data/%s/Rodada%s/"
       "partidas_#%s.txt"
       )
scoutsFile = '.\\data\\%s\\scouts.csv'%ano
scouts = pd.read_csv(scoutsFile, sep = ';', decimal=',',header = 0, index_col=[0,1])

partidas=[]
for rod in range(1,39):
    part = pd.read_csv(repo%(ano,rod,rod),
                       sep = '\t',
                       header = 0,
                       encoding = 'utf-8',
                       index_col = 0,
                      )
    part['rodada'] = rod
    partidas.append(part)

partidas = pd.concat(partidas, axis = 0)
partidas.reset_index(inplace=True)

scouts.reset_index(inplace=True)
scouts['rodada'] = pd.to_numeric(scouts.reset_index()['RODADA'].str.split('_',expand=True)[1])
gProM = scouts[scouts.LOCAL=='CASA'].groupby(['rodada','CLUBE'])['G'].sum()
gProV = scouts[scouts.LOCAL=='FORA'].groupby(['rodada','CLUBE'])['G'].sum()

advIndex = scouts[scouts.LOCAL=='CASA'].groupby(['rodada','CLUBE'])['ADV'].min()
gcM = pd.DataFrame(scouts[scouts.LOCAL=='CASA'].groupby(['rodada','CLUBE'])['GC'].sum())
gcV = pd.DataFrame(scouts[scouts.LOCAL=='FORA'].groupby(['rodada','CLUBE'])['GC'].sum())

gcM['para'] = advIndex
gcM = gcM.reset_index().set_index(['rodada','para'])['GC']
gcM.index.names = ['rodada','CLUBE']

advIndex = advIndex.reset_index().set_index(['rodada','ADV'])
gcV['para'] = advIndex
gcV = gcV.reset_index().set_index(['rodada','para'])['GC']
gcV.index.names = ['rodada','CLUBE']

partidas = partidas.set_index(['rodada','MANDANTE'])
partidas['gol_mandante'] = gProM + gcV

partidas = partidas.reset_index().set_index(['rodada','VISITANTE'])
partidas['gol_visitante'] = gProV + gcM

partidas.reset_index(inplace=True)

#Olhar partidas com valida = False individualmente depois

partidas['validaCartola'] = partidas['VALIDA'].copy()
partidas['ano'] = ano
partidas['data'] = partidas['DATA'].str.cat(['/2018']*len(partidas))
partidas['data'] = pd.to_datetime(partidas['data'].str.cat(others = partidas['HORARIO'], sep=' '), dayfirst=True).apply(timezone.make_aware)
partidas['mandante'] = partidas['MANDANTE'].apply(lambda x: Clube.objects.get(nome=x))
partidas['visitante'] = partidas['VISITANTE'].apply(lambda x: Clube.objects.get(nome=x))
partidas['estadio'] = partidas['LOCAL'].apply(lambda x: Estadio.objects.get(nome=x))

toDB = partidas[['mandante','visitante','gol_mandante','gol_visitante','data','ano','rodada','validaCartola','estadio']].copy()
toDB.apply(lambda x: Partida.objects.update_or_create(**x), axis = 1)
