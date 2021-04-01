#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:31:21 2020

@author: lucas
"""

import pandas as pd
import utm

def utm_tolatlon(x,y):    
    u = utm.to_latlon(x,y,zone_letter='J',zone_number=21)
    return u



names = [ 'id','parque','east','north','operacao_comercial' ]
da=pd.read_excel('~/dados_vento/CoordenadasAeroseTorresCerroChato.xls',\
                 header=None, names=names, skiprows=1)
east, north = da.east, da.north

lon_lat = []
for i in range(len(da.east)):
    x,y = utm_tolatlon(east[i],north[i])
    var = x,y
    lon_lat.append(var)
    
df = pd.DataFrame(lon_lat, columns=['lat','lon'])
df.to_csv('~/dados_vento/lat_lon_towers.txt')
#df = pd.DataFrame(lon_lat,columns=['lon','lat'])
