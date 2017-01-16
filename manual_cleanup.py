"""Utility module for working with Apollo Heat Flow Experiment data."""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.ion() # Don't lock up the terminal when displaying a plot.

ipath = '../../heat_flow_experiment_hfe/data/PSPG-00752_1284752997_APOLLO15_HDF_1/'

datafiles = ['a15p1.file_1','a15p1.file_3','a15p1.file_5','a15p2.file_2',
             'a15p2.file_4','a15p1.file_2','a15p1.file_4','a15p2.file_1',
             'a15p2.file_3','a15p2.file_5']

data = {}
for f in datafiles:
    mission = f[:3]
    if not mission in data.keys():
        data[mission] = {}
    probe = f[3:5]
    if not probe in data[mission].keys():
        data[mission][probe] = {}
    sensor = int(f[-1:])
    columns = (['Time','HTR','TREF','TC1','TC2','TC3','TC4']
                                    if sensor is '3' else ['Time','T','dT'])
    data[mission][probe][sensor] = pd.read_csv('{i}{f}'.format(
        i=ipath,f=f),skiprows=1,names=columns,delim_whitespace=True,
                                skipinitialspace=True)#,skipfooter=1)

def plot_rollovers():
    # The signal is rolling over at T of 2/2**n
    plt.axhline(y=0.0, color='r', linestyle='-')
    for p in range(10):
        plt.axhline(y=-2./2**p, color='r', linestyle='-')

# Don't even look at entries with bad values.
ix = np.where((Time!=-9999) & (T!=-9999) & (dT!=-9999))
Time = np.array(data['a15']['p1'][1]['Time'])[ix]
T = np.array(data['a15']['p1'][1]['T'])[ix]
dT = np.array(data['a15']['p1'][1]['dT'])[ix]

# plt.figure()
# plt.plot(Time,T,'.')
# plt.xlabel('Time')
# plt.ylabel('Temp')
# plot_rollovers()
# plt.ylim([-5,5])
# plt.figure()
# plt.plot(T,'.')
# plt.xlabel('n')
# plt.ylabel('Temp')
# plot_rollovers()
# plt.ylim([-5,5])


bins=np.array([-2./2**n for n in range(10)])
# [-2., -1., -0.5, -0.25, -0.125, -0.0625, -0.0313, -0.0156, -0.008, -0.004]
T[0:31] = 2*bins[1]-T[0:31]
T[31:150] = 2*bins[0]-T[31:150]
T[150:208] = 2*bins[1]-T[150:208]
T[208:229] = 2*bins[2]-T[208:229]
T[229:235] = 2*bins[3]-T[229:235]
T[235:238] = 2*bins[4]-T[235:238]
T[238:239] = 2*bins[5]-T[238:239]
T[239:240] = 2*bins[6]-T[239:240]
T[240:241] = 2*bins[7]-T[240:241]
T[241:1494] = T[241:1494] # >0
T[1494:1495] = T[1494:1495] # Ambiguous.
T[1495:1496] = 2*bins[-1]-T[1495:1496]
T[1496:1499] = 2*bins[-2]-T[1496:1499]
T[1499:1504] = 2*bins[-3]-T[1499:1504]
T[1504:1511] = 2*bins[-4]-T[1504:1511]
T[1511:1530] = 2*bins[-5]-T[1511:1530]
T[1530:1569] = 2*bins[-6]-T[1530:1569]
T[1569:1648] = 2*bins[-7]-T[1569:1648]
T[1648:1954] = 2*bins[-8]-T[1648:1954]
T[1954:2415] = 2*bins[-9]-T[1954:2415]
T[2415:2447] = 2*bins[-8]-T[2415:2447]
T[2447:2459] = 2*bins[-7]-T[2447:2459]
T[2459:2464] = 2*bins[-6]-T[2459:2464]
T[2464:2467] = 2*bins[-5]-T[2464:2467]
T[2467:2468] = 2*bins[-3]-T[2467:2468] # Ambiguous.
T[2468:2990] = T[2468:2990]

plt.close('all')
plt.figure()
plt.plot(T,'.')
plt.xlim([0,3000])
plt.ylim([-5,5])
plt.xlabel('n')
plt.ylabel('Temp')
plot_rollovers()
