#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:59:24 2020

@author: lucas

Objetivo: prepadar o dado de entrada para ensemble methods
sckitlearn.

y_shape = 2880 -> 48 horas de observação media dos 10min
x_shape = (2880,x) -> saída wrf com x features, com valores a cada 10min em 48h

"""

import pandas as pd
import numpy as np
from netCDF4 import Dataset
import wrf
import glob
import datetime as dt



torres = pd.read_csv('/home/lucas/dados_vento/lat_lon_towers.txt', usecols=[1,2]).values
date = dt.datetime(2018,5,22,21)
delta = dt.timedelta(hours=1)
wind_f=[]
#l = [glob.glob('/media/lucas/ce7c746b-5271-4ebe-a443-a00fe8fb43f4/wrf/WRF/run/wrfout_d02*')]
#print(len(l))
for i in range(0,55):

	
	#date = dt.datetime(2018,5,22,18)
	#delta = dt.timedelta(hours=1)
	day = date.day
	hour = date.hour
	date += delta
	fl=[]
	while i <=55:
		f = glob.glob('/media/lucas/ce7c746b-5271-4ebe-a443-a00fe8fb43f4/wrf/WRF/run/wrfout_d02_2018-05-{:02d}*'.format(day))
		fl.append(f)
		i+=1
	#print(f)
	
	
	
	
	wrfile = Dataset(fl[i])
	#'/media/lucas/ce7c746b-5271-4ebe-a443-a00fe8fb43f4/wrf/WRF/run/wrfout_d02_2018-05-{:02d}_{:02d}:00:00'.format(day,hour))
	wspd = wrf.getvar(wrfile, 'wspd_wdir', units='m/s')[0].values
	lon = wrf.getvar(wrfile, 'lon').values
	lat = wrf.getvar(wrfile, 'lat').values

	n=0
	coordenada=[]
	wind=[]
	while n<3:
	    	abslat = np.abs(lat-torres[n,0])
	    	abslon = np.abs(lon-torres[n,1])
	    	c = np.maximum(abslon,abslat)
	    	x, y = np.where(c == np.min(c))
	    	wind_ = wspd[0,x,y]
	    	print(wind_)
	    	wind.append(wind_)
	    	n+=1	


'''		
#print(len(wind_))
		
		
#		wind_f.append(wind)
	
#	except:
#		pass
#print(wind_)
#print('\n')
	
	
	
	

	
#print(len(wind_f))
    #indx = x , y
#    print(wspd[indx])
    #if n==2:
    	#print(wspd[0,x,y].values)   
#    coordenada.append(indx)
#    n+=1
	
	
	
	
#wrfout_d02_2018-05-23_04_00_00

ecc1 = pd.read_csv('~/dados_vento/ecc1_.csv')
ecc1 = pd.DataFrame(ecc1)
vs_med = ecc1.vs_med.values
vs_dev = ecc1.vs_dev.values
vs_max = ecc1.vs_max.values
vs_min = ecc1.vs_min.values

wrfile = Dataset('/media/lucas/ce7c746b-5271-4ebe-a443-a00fe8fb43f4/wrf/WRF/run/wrfout_d02_2018-05-23_09:00:00')

wspd = wrf.getvar(wrfile, 'wspd_wdir', units='m/s')[0]
torres = pd.read_csv('/home/lucas/dados_vento/lat_lon_towers.txt', usecols=[1,2]).values
lat = wrf.getvar(wrfile, 'lat').values
lon = wrf.getvar(wrfile, 'lon').values

n=0
coordenada = []
while n<3:
    abslat = np.abs(lat-torres[n,0])
    abslon = np.abs(lon-torres[n,1])
    c = np.maximum(abslon,abslat)
    x, y = np.where(c == np.min(c))
    n+=1
    wspd[0,x,y].values
    #indx = x , y
#    print(wspd[indx])
    #if n==2:
    	print(wspd[0,x,y].values)   
#    coordenada.append(indx)
#    n+=1
    
    
 
#print(coordenada[0])







'''
