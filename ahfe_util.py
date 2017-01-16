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

# plt.ion()
# for p in data['a15'].keys():
#     #plt.figure()
#     #plt.title(p)
#     for s in data['a15'][p].keys():
#         if s is 3:
#             continue
#
#         plt.figure()
#         plt.title('{p}:{s}:T'.format(p=p,s=s))
#         plt.plot(data['a15'][p][s]['Time'][data['a15'][p][s]['T']!=-9999],
#                  data['a15'][p][s]['T'][data['a15'][p][s]['T']!=-9999],label=s)
#
#         #plt.figure()
#         #plt.title('{p}:{s}:dT'.format(p=p,s=s))
#         #plt.plot(data['a15'][p][s]['Time'][data['a15'][p][s]['T']!=-9999],
#         #         data['a15'][p][s]['dT'][data['a15'][p][s]['T']!=-9999],
#         #         '.',label=s)
#
# plt.show()

# Apollo 15 -- p1 is the sensor with the data problem
Time = np.array(data['a15']['p1'][1]['Time'])
T = np.array(data['a15']['p1'][1]['T'])
dT = np.array(data['a15']['p1'][1]['dT'])
# Don't even look at entries with bad values.
ix = np.where((Time!=-9999) & (T!=-9999) & (dT!=-9999))

plt.figure()
# The signal is rolling over at T of 2/2**n
plt.plot(Time[ix][5000:10000],T[ix][5000:10000],'.')
#plt.plot(Time[ix],cleanup(T[ix]),'x')
plt.axhline(y=0.0, color='r', linestyle='-')
for p in range(6):
    plt.axhline(y=-2./2**p, color='r', linestyle='-')
plt.ylim([-2.1,0.1])

def cleanup(s):
    b = []
    offset = 0
    trend = 'down'
    bins=np.array([-2./2**n for n in range(7)])
    for i,_ in enumerate(s):
        if (i==0) | (i==len(s)-1):
            b+=[s[i]]
            continue
        elif s[i]>=0.0:
            b+=[s[i]]
            continue

        # Is the temp headed down or up?
        if (b[-1]>0) & (max(bins)<s[i]<0):
            trend = 'down'
            offset = bins[np.digitize(s[i+1],bins)-1]
        elif (b[-1]<-2) & (max(bins)<s[i]<0):
            print('{b}, {s}'.format(b=b[-1],s=s[i]))
            offset = bins[0]
        #    b+=[2*offset-s[i]]
            trend = 'up'
            #continue

        b+=[2*offset-s[i]]
        if ((s[i-1]<s[i]) & (s[i+1]<s[i])):# & (0.15<s[i]<0.0)):# &
            #(max(s[i]-s[i-1],s[i]-s[i+1])>abs(s[i-1]-s[i-2]))):
            if (trend is 'down') & (abs(s[i]-s[i-1])<abs(s[i]-s[i+1])):
                #offset = bins[np.digitize(s[i+1],bins)-1]
                offset = bins[np.digitize(offset,bins)-2]
            elif (trend is 'up') & (abs(s[i]-s[i-1])>abs(s[i]-s[i+1])):
                #offset = bins[np.digitize(b[-1],bins)+1]
                offset = bins[np.digitize(offset,bins)]
                b[-1]=2*offset-s[i]
        #        print(offset)
        #else:
        #    b+=[2*offset-s[i]]

    return b

plt.figure()
ix = np.where((Time!=-9999) & (T!=-9999) & (dT!=-9999))
plt.plot(Time[ix][10000:13000],T[ix][10000:13000],'.')
plt.plot(Time[ix][10000:13000],cleanup(T[ix][10000:13000]),'x')
plt.axhline(y=0.0, color='r', linestyle='-')
for p in range(7):
    plt.axhline(y=-2./2**p, color='r', linestyle='-')

# ix = np.where((Time!=-9999) & (T!=-9999) & (dT!=-9999))
# plt.plot(Time[ix],T[ix],'.')
# plt.plot(Time[ix],cleanup(T[ix]),'x')
# plt.axhline(y=0.0, color='r', linestyle='-')
# for p in range(7):
#     plt.axhline(y=-2./2**p, color='r', linestyle='-')
