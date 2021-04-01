from netCDF4 import Dataset
import wrf
import numpy as np
import pandas as pd

import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader
import cartopy.feature as cfe
from cartopy import config
from cartopy.feature import ShapelyFeature

from matplotlib.cm import get_cmap
from matplotlib.image import imread
import matplotlib.pyplot as plt

from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


# LER AQUIVOS

# torres anemométricas, dados geográficos, saída wrf, shapefile
torres_path = '/home/lucas/dados_vento/lat_lon_towers.txt'
torres = pd.read_csv(torres_path, usecols=[1,2]).values

geogrid_path = '/media/lucas/ce7c746b-5271-4ebe-a443-a00fe8fb43f4/wrf/WRF/run/geo_em.d03.nc'
geogrid_path1 = '/home/lucas/dados_vento/dominios/test/geo_em.d02.nc'
geogrid = Dataset(geogrid_path1)

wrf_path = '/media/lucas/ce7c746b-5271-4ebe-a443-a00fe8fb43f4/wrf/WRF/run/wrfout_d03_2018-05-22_18:30:00'
wrfile = Dataset(wrf_path)

path_shpfile = '/home/lucas/dados_vento/shapefile/Municipios_IBGE.shp'
shpfile = Reader(path_shpfile)


# LER CAMPOS

topografia = wrf.getvar(geogrid, "HGT_M")
#lat = wrf.getvar(geogrid, "lat")
#lon = wrf.getvar(geogrid, "lon")
wspeed = wrf.getvar(wrfile,'wspd_wdir')[0]
wdir = wrf.getvar(wrfile,'wspd_wdir')[1]

# LER DADOS TORRES

da = pd.read_csv('/home/lucas/dados_vento/lat_lon_towers.txt',\
			 usecols=[1,2])
lat = da.lat.values
lon = da.lon.values

# LER PROJEÇÃO CARTOGRÁFICA DO WRF




cart_proj = wrf.get_cartopy(topografia)
lats, lons = wrf.latlon_coords(topografia)

# CRIAR FIGURA

width = 800
height = 800
dpi = 96
resolution = '10m'

fig = plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)
ax = plt.axes(projection=cart_proj)
ax.add_geometries(shpfile.geometries(), \
		crs=ccrs.Geodetic(), edgecolor='k', \
		 facecolor='none')
ax.coastlines()
ax.add_feature(cfe.NaturalEarthFeature('cultural',\
		 'admin_1_states_provinces_lines', resolution, \
                                            edgecolor='gray',\
                                             facecolor='none'))
ax.coastlines(resolution='50m', color='black', linewidth=1)


# IDENTIFICAR TORRES NO MAPA
ax.plot(lon[:3], lat[:3], 'g^',color='black', markersize=10,\
		 transform=ccrs.Geodetic())
ax.plot(lon[3:], lat[3:],'.',color='gray', markersize=5,\
		 transform=ccrs.Geodetic())


# CONTORNOS
plt.contourf(wrf.to_np(lons), wrf.to_np(lats),\
			 wrf.to_np(topografia), 10, \
                transform=ccrs.PlateCarree(), cmap=get_cmap("Reds"))


# "COLORBAR"
cbar = plt.colorbar(ax=ax, shrink=0.62)
cbar.set_label(topografia.units)

# configurando os limites do mapa, nesse caso não é necessário
ax.set_xlim(wrf.cartopy_xlim(topografia))
ax.set_ylim(wrf.cartopy_ylim(topografia))

# LINHAS DE GRADE
ax.gridlines(color="black", linestyle="dotted")

# TÍTULO
plt.title(topografia.description+'\n'+str(topografia.Time.values))


# Add arrows to show the wind vectors !!!!
u10 = wrf.getvar(wrfile, 'U10')
v10 = wrf.getvar(wrfile, 'V10')


nx = wrfile.dimensions['west_east'].size
ny = wrfile.dimensions['south_north'].size

dt, dx, dy = wrfile.DT, wrfile.DX, wrfile.DY

cen_lat, cen_lon = wrfile.CEN_LAT, wrfile.CEN_LON
truelat1, truelat2, STAND_LON = wrfile.TRUELAT1, wrfile.TRUELAT2, wrfile.STAND_LON
pole_lat, pole_lon = wrfile.POLE_LAT, wrfile.POLE_LON


cone = 1 # ???
uv   = wrf.uvmet(u10, v10, u10.XLONG, u10.XLAT,
                     cen_lon, cone, meta=True, units='m s-1')
x = u10.XLONG.values
y = u10.XLAT.values
u = uv[0].values
v = uv[1].values


Q = plt.quiver( x, y, u, v,
               pivot='middle',
               transform=ccrs.PlateCarree(),
               regrid_shape=20
               )

### plot quiver key
qk = plt.quiverkey(Q,
                   1.07, 0.99,                  # x,y label position
                   10, str(10)+' '+u10.units, # choose units + update string
                   labelpos='E',                # add label to the right
                   coordinates='axes'
                   )
# mostrar figura
plt.show()
