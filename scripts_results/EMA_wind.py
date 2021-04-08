from netCDF4 import Dataset
import numpy as np
import glob
import os
import pandas as pd
import wrf
import datetime
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
import cartopy.feature as cfeature
from cartopy import config
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.feature import ShapelyFeature
from sklearn.metrics import mean_absolute_error,mean_squared_error
from matplotlib.cm import get_cmap
import matplotlib.pyplot as plt
from matplotlib.image import imread

for caso in range(1,3):
    
    for membro in range(1,10):

        

        BASE_DIR = os.path.abspath('/media/lucasdmarten/HD/DADOS_TCC/RESULTADOS/')

        # MODELO
        wrfcsv =  pd.read_csv(BASE_DIR+'/CASO{}/MEMBRO{}/c{}.m{}.csv'.format(caso,membro,caso,membro), usecols=[0,1,2,4,7,8,9,10,11])
        geo = Dataset('/media/lucasdmarten/HD/wrf/domains/firstDomainPC/geo_em.d01.nc')


        # OBS
        dfcompara = pd.read_csv('../tcc/data/ecc3_.csv', usecols=[0,3,4,5,6,10,12,16,18])
        if caso == 1:
            dfcompara = dfcompara[(dfcompara.data>'2018-05-23') & (dfcompara.data<'2018-05-25')]
            wrfcsv = wrfcsv[(wrfcsv.times>'2018-05-23') & (wrfcsv.times<'2018-05-25')]
            di = datetime.datetime(2018,5,23,0)
            df = datetime.datetime(2018,5,25,0)

        else:
            dfcompara = dfcompara[(dfcompara.data>'2018-09-23') & (dfcompara.data<'2018-09-25')]
            wrfcsv = wrfcsv[(wrfcsv.times>'2018-09-23') & (wrfcsv.times<'2018-09-25')]
            di = datetime.datetime(2018,9,23,0)
            df = datetime.datetime(2018,9,25,0)


        dates = []
        while di < df:
            dates.append(di)
            di += datetime.timedelta(hours=1)

        # newdates=[]
        # for i in range(len(dates)):
        #     date_obj = datetime.datetime.strptime(dates[i], '%Y-%m-%d %H:%M:%S')
        #     newdates.append('{:02d}/{:02d} - {:02d}hrs'.format(date_obj.day,date_obj.month,date_obj.hour))


        tamanho=len(wrfcsv)
        ev_at108=[]
        ed_at106=[]
        ev_at88=[]
        ev_at67=[]
        ed_at65=[]
        for i in range(tamanho):
        #     p_psfc
        #     p_t2
        #     p_ur
            p_vs_108 = wrfcsv.wspd108.values[i]
            p_ds_106 = wrfcsv.wdir106.values[i]
            p_vi_67 = wrfcsv.wspd67.values[i]
            p_di_65 = wrfcsv.wdir65.values[i]
            p_vm_88 = wrfcsv.wspd88.values[i]
            
            vs_108 = dfcompara.vs_med.astype('float').values[i]
            ds_106 = dfcompara.ds_med.astype('float').values[i]
            vi_67 = dfcompara.vi_med.astype('float').values[i]
            di_65 = dfcompara.di_med.astype('float').values[i]
            vm_88 = dfcompara.vm_med.astype('float').values[i]
            
            ev_at108.append(vs_108-p_vs_108)
            ed_at106.append(ds_106-p_ds_106)
            ev_at88.append(vm_88-p_vm_88)
            ev_at67.append(vi_67-p_vi_67)
            ed_at65.append(di_65-p_di_65)
            



        print("EMA para vs_108")
        print(mean_absolute_error(list(wrfcsv.wspd108.values),dfcompara.vs_med.astype('float').to_list()))
        wspd108_EMA = mean_absolute_error(list(wrfcsv.wspd108.values),dfcompara.vs_med.astype('float').to_list())
        print('\n'*2)
        print("EMA para ds_106")
        print(mean_absolute_error(list(wrfcsv.wdir106.values),dfcompara.ds_med.astype('float').to_list()))
        wdir106_EMA =  mean_absolute_error(list(wrfcsv.wdir106.values),dfcompara.ds_med.astype('float').to_list())
        print('\n'*2)
        print("EMA para vi_67")
        print(mean_absolute_error(list(wrfcsv.wspd67.values),dfcompara.vi_med.astype('float').to_list()))
        wspd67_EMA = mean_absolute_error(list(wrfcsv.wspd67.values),dfcompara.vi_med.astype('float').to_list())
        print('\n'*2)
        print("EMA para di_65")
        print(mean_absolute_error(list(wrfcsv.wdir65.values),dfcompara.di_med.astype('float').to_list()))
        wdir65_EMA = mean_absolute_error(list(wrfcsv.wdir65.values),dfcompara.di_med.astype('float').to_list())
        print('\n'*2)
        print("EMA para vm_88")
        print(mean_absolute_error(list(wrfcsv.wspd88.values),dfcompara.vm_med.astype('float').to_list()))
        wspd88_EMA = mean_absolute_error(list(wrfcsv.wspd88.values),dfcompara.vm_med.astype('float').to_list())

        '''

        pega csv criado a partir dos dados do wrf e calcula o obs - prev

        '''
        pd.DataFrame({
            "wspd108_EMA":wspd108_EMA, "wdir106_EMA":wdir106_EMA, "wspd67_EMA":wspd67_EMA, "wdir65_EMA":wdir65_EMA,
            "wspd88_EMA":wspd88_EMA
            }, index=False).to_csv('./erro_m{}_c{}.csv'.format(membro,caso), index=None)

        
            