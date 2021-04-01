from netCDF4 import Dataset
import numpy as np
import glob
import os
import pandas as pd
import wrf

import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
import cartopy.feature as cfeature
from cartopy import config
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.feature import ShapelyFeature

from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt
from matplotlib.image import imread

wrfile_d02 = Dataset('/media/lucas/ce7c746b-5271-4ebe-a443-a00fe8fb43f4/wrf/WRF/run/wrfout_d02_2018-05-23_13:00:00')
torres = pd.read_csv('/home/lucas/dados_vento/lat_lon_towers.txt', usecols=[1,2]).values
topo = Dataset('/media/lucas/ce7c746b-5271-4ebe-a443-a00fe8fb43f4/wrf/WRF/run/geo_em.d02.nc')

wspeed = wrf.getvar(wrfile_d02,'wspd_wdir')[0]
wdir = wrf.getvar(wrfile_d02,'wspd_wdir')[1]
z = wrf.getvar(wrfile_d02, 'z', units='m')
slp = wrf.getvar(wrfile_d02,'slp')
p = wrf.getvar(wrfile_d02,'pressure')
lon = wrf.getvar(wrfile_d02,'lon')
lat = wrf.getvar(wrfile_d02,'lat')
t2 = wrf.getvar(wrfile_d02,'T2')
geo = wrf.getvar(topo, 'HGT_M')


a = wrf.interplevel(wspeed, z, 
                    
                    [310.52426  +  108,   337.42102 + 108,   300.4599 + 108]
                    
                   )
n=0
coordenada=[]
wind=[]
topografia=[]
while n<3:
    abslat = np.abs(lat-torres[n,0])
    abslon = np.abs(lon-torres[n,1])
    c = np.maximum(abslon,abslat)
    x, y = np.where(c == np.min(c))
    wind_ = a[1,x,y]
    topografia_ = geo[x,y]
    wind.append(wind_)
    topografia.append(topografia_)
    n+=1

    

    

df = pd.read_csv('ecc1_.csv')
df2 = pd.read_csv('ecc2_.csv')
df3 = pd.read_csv('ecc3_.csv')

vi_max_1 = float(df[df.data=='2018-05-23 13:00:00']['vi_max'])
vi_max_2 = float(df2[df2.data=='2018-05-23 13:00:00']['vi_max'])
vi_max_3 = float(df3[df3.data=='2018-05-23 13:00:00']['vi_max'])

print(" Valor observado: {}\n Valor previsto pelo WRF: {}".format(wind[0].values, vi_max_1))