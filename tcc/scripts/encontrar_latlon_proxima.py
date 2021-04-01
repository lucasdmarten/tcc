#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:41:29 2020

@author: lucas
"""


from netCDF4 import Dataset
import numpy as np
from pandas import read_csv
from wrf import getvar

wrfile = Dataset('/media/lucas/ce7c746b-5271-4ebe-a443-a00fe8fb43f4/wrf/WRF/run/wrfout_d02_2018-05-23_00:00:00')
torres = read_csv('/home/lucas/dados_vento/lat_lon_towers.txt', usecols=[1,2]).values
lat = getvar(wrfile, 'lat').values
lon = getvar(wrfile, 'lon').values

n=0
coordenada = []
while n<3:
    abslat = np.abs(lat-torres[n,0])
    abslon = np.abs(lon-torres[n,1])
    c = np.maximum(abslon,abslat)
    x, y = np.where(c == np.min(c))
    indx = x , y
    coordenada.append(indx)
    n+=1
    
    
for i in coordenada:
    print( lat[i], lon[i] )