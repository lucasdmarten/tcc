import matplotlib.pyplot as plt
from pandas import read_csv
import datetime as dt
from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)


press = read_csv('/home/lucas/tcc/inmet/dado_cicl.txt').pressao
data = [dt.datetime.strptime(read_csv('/home/lucas/tcc/inmet/dado_cicl.txt').data[i]+' UTC '+str(read_csv('/home/lucas/tcc/inmet/dado_cicl.txt').hora[i]),
                "%d/%m/%Y UTC %H") for i in range(len(press))]
formatter = DateFormatter('%d/%m  %HUTC')
fig, ax = plt.subplots(figsize=((800/96),(800/96)), dpi=96)
ax.plot(data,press)
plt.title('Pressão - Estação automática Capão do Leão - RS')
plt.grid()
plt.xlabel('Tempo')
plt.ylabel('Vento (m/s)')
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)

press = read_csv('/home/lucas/tcc/inmet/dado_cicl2.txt').pressao
data = [dt.datetime.strptime(read_csv('/home/lucas/tcc/inmet/dado_cicl2.txt').data[i]+' UTC '+str(read_csv('/home/lucas/tcc/inmet/dado_cicl2.txt').hora[i]),
                "%d/%m/%Y UTC %H") for i in range(len(press))]
formatter = DateFormatter('%d/%m  %HUTC')
fig, ax = plt.subplots(figsize=((800/96),(800/96)), dpi=96)
ax.plot(data,press)
plt.title('Pressão - Estação automática Capão do Leão - RS')
plt.grid()
plt.xlabel('Tempo')
plt.ylabel('Vento (m/s)')
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
