#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 22:26:51 2020

@author: lucas
"""
import os
import matplotlib.pyplot as plt
from cartopy import config
import cartopy.crs as ccrs
import os
from matplotlib.image import imread
import numpy as np
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature
from cartopy.io.shapereader import Reader
import pandas as pd
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

da = pd.read_csv('/home/lucas/dados_vento/lat_lon_towers.txt', usecols=[1,2])
lat = da.lat.values
lon = da.lon.values

# Não sei...
fname = os.path.join(config["repo_data_dir"],
                     'raster', 'natural_earth', '50-natural-earth-1-downsampled.png')
img = plt.imread(fname)
img2 = np.ones(img.shape)
###

width = 800
height = 800
dpi = 96
resolution = '50m'

def plot_():

    img_extent = (-55.78, -55.63, -30.88, -30.775)
    fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.imshow(img2, origin='upper', extent=img_extent, transform=ccrs.PlateCarree())
    ax.coastlines()
    ax.add_feature(cfeature.NaturalEarthFeature('cultural', 'admin_0_countries', resolution, edgecolor='black', \
                                                facecolor='none'))
    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'lakes', resolution, edgecolor='none', \
                                                facecolor=cfeature.COLORS['water']), alpha=0.01)
    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'rivers_lake_centerlines', resolution, \
                                                edgecolor=cfeature.COLORS['water'], facecolor='none'))
    ax.add_feature(cfeature.NaturalEarthFeature('cultural', 'admin_1_states_provinces_lines', resolution, \
                                                edgecolor='gray', facecolor='none'))
    ax.coastlines(resolution='50m', color='black', linewidth=1)

    ax.plot(lon[:3], lat[:3], 'g^',color='black', markersize=7, transform=ccrs.Geodetic())
    ax.plot(lon[3:], lat[3:],'3',color='gray', markersize=10, transform=ccrs.Geodetic())
    ax.legend(('Torres de medição','Turbinas eólicas'),loc='upper left',fontsize=12)#, label='Inline label')
    #ax.text(-117, 33, 'San Diego', transform=ccrs.Geodetic())
    gl = ax.gridlines(draw_labels=True, crs=ccrs.PlateCarree())
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabels_top = False
    
    plt.title(label='Torres eólicas e anemométricas - Santana do Livramento/RS',loc='center', fontsize=12)
    plt.savefig('/home/lucas/dados_vento/v1_plot.png')
    return    plt.show()
plot_()