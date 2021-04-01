#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 14:56:21 2020

PEGAR DADOS DAS TORRES ANEMOMÉTRICAS E CONVERTER AS DATAS QUE ESTAVAM EM DUAS
COLUNAS: DATA(YYYYMMDD) E HORA(HHMMSS)

CONVERTER PARA: DATETIME

PASSAR PARA CSV.


@author: lucas
"""

import pandas as pd
import datetime as dt

names = ['data','hora','erro','hPa','tp','ur','vs_med','vs_max','vs_min',\
        'vs_dev','ds_med','ds_dev','vi_med','vi_max','vi_min','vi_dev',\
        'di_med','di_dev','vm_med','vm_max','vm_min','vm_dev']

ecc1 = pd.read_excel('~/dados_vento/ECC1.xlsx', skiprows=23, names=names)
ecc1 = pd.DataFrame(ecc1)
ecc2 = pd.read_excel('~/dados_vento/ECC2.xlsx', skiprows=23, names=names)
ecc2 = pd.DataFrame(ecc2)
ecc3 = pd.read_excel('~/dados_vento/ECC3.xlsx', skiprows=23, names=names)
ecc3 = pd.DataFrame(ecc3)

data_1 = pd.date_range('2018-5-23 00:00', '2018-5-23 23:50', periods=144)
data_2 = pd.date_range('2018-5-24 00:00', '2018-5-24 23:50', periods=144)
data_3 = pd.date_range('2018-6-30 00:00', '2018-6-30 23:50', periods=144)
data_4 = pd.date_range('2018-7-24 00:00', '2018-7-24 23:50', periods=144)
data_5 = pd.date_range('2018-9-01 00:00', '2018-9-01 23:50', periods=144)
data_6 = pd.date_range('2018-9-11 00:00', '2018-9-11 23:50', periods=144)
data_7 = pd.date_range('2018-9-23 00:00', '2018-9-23 23:50', periods=144)
data_8 = pd.date_range('2018-9-24 00:00', '2018-9-24 23:50', periods=144)
data_9 = pd.date_range('2018-9-30 00:00', '2018-9-30 23:50', periods=144)
data_10 = pd.date_range('2018-10-01 00:00', '2018-10-01 23:50', periods=144)
data_11 = pd.date_range('2018-12-24 00:00', '2018-12-24 23:50', periods=144)

datas = [data_1,data_2,data_3,data_4,data_5,data_6,data_7,data_8,data_9,\
         data_10,data_11]
alcance_loop =  range(0,1584+144,144)

step = 144
i=0
idx=0
while i < 1584:
    ecc1.data.iloc[i:step] = datas[idx]
    ecc2.data.iloc[i:step] = datas[idx]
    ecc3.data.iloc[i:step] = datas[idx]
    #print(i)
    #print(step)
    #print(idx)
    #print('----'*10)
    idx+=1
    i+=144
    step+=144
    
    
ecc1.to_csv('~/dados_vento/ecc1_.csv',index=False)
ecc2.to_csv('~/dados_vento/ecc2_.csv',index=False)
ecc3.to_csv('~/dados_vento/ecc3_.csv',index=False)
    
