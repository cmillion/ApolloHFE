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
T[2468:2990] = T[2468:2990] # >0
T[2990:2991] = T[2990:2991] # Ambiguous.
T[2991:2992] = 2*bins[6]-T[2991:2992] # Ambiguous.
T[2992:2994] = 2*bins[5]-T[2992:2994] # Slightly ambiguous.
T[2994:2999] = 2*bins[4]-T[2994:2999]
T[2999:3008] = 2*bins[3]-T[2999:3008]
T[3008:3028] = 2*bins[2]-T[3008:3028]
T[3028:3090] = 2*bins[1]-T[3028:3090]
T[3090:3146] = 2*bins[0]-T[3090:3146]
T[3146:3228] = 2*bins[1]-T[3146:3228]
T[3228:3250] = 2*bins[2]-T[3228:3250]
T[3250:3258] = 2*bins[3]-T[3250:3258]
T[3258:3263] = 2*bins[4]-T[3258:3263]
T[3263:3266] = 2*bins[5]-T[3263:3266]
T[3266:3267] = 2*bins[6]-T[3266:3267] # Ambiguous.
T[3267:3760] = T[3267:3760] # >0
T[3760:3761] = T[3760:3761] # Ambiguous.
T[3761:3762] = T[3761:3762] # Ambiguous.
T[3762:3764] = 2*bins[5]-T[3762:3764]
T[3764:3767] = 2*bins[4]-T[3764:3767]
T[3767:3776] = 2*bins[3]-T[3767:3776]
T[3776:3793] = 2*bins[2]-T[3776:3793]
T[3793:3843] = 2*bins[1]-T[3793:3843]
T[3843:3981] = 2*bins[0]-T[3843:3981]
T[3981:4036] = 2*bins[1]-T[3981:4036]
T[4036:4050] = 2*bins[2]-T[4036:4050]
T[4050:4056] = 2*bins[3]-T[4050:4056]
T[4056:4059] = 2*bins[4]-T[4056:4059]
T[4059:4061] = 2*bins[5]-T[4059:4061] # Slightly ambiguous.
T[4061:4062] = 2*bins[6]-T[4061:4062] # Slightly ambiguous.
T[4062:4063] = 2*bins[8]-T[4062:4063] # Ambiguous
T[4063:4524] = T[4063:4524] # >0
T[4524:4525] = T[4524:4525] # Ambiguous
T[4525:4526] = T[4525:4526] # Ambiguous
T[4526:4527] = T[4526:4527] # Ambiguous
T[4527:4529] = 2*bins[-5]-T[4527:4529]
T[4529:4533] = 2*bins[-6]-T[4529:4533]
T[4533:4542] = 2*bins[-7]-T[4533:4542]
T[4542:4559] = 2*bins[-8]-T[4542:4559]
T[4559:4601] = 2*bins[-9]-T[4559:4601]
T[4601:4775] = 2*bins[0]-T[4601:4775]
T[4775:4821] = 2*bins[1]-T[4775:4821]
T[4821:4833] = 2*bins[2]-T[4821:4833]
T[4833:4840] = 2*bins[3]-T[4833:4840]
T[4840:4845] = 2*bins[4]-T[4840:4845]
T[4845:4847] = 2*bins[5]-T[4845:4847]
T[4847:4848] = 2*bins[6]-T[4847:4848] # Slightly ambiguous.
T[4848:4849] = 2*bins[7]-T[4848:4849] # Slightly ambiguous.
T[4849:5295] = T[4849:5295] # >0
T[5295:5296] = 2*bins[-3]-T[5295:5296] # Ambiguous.
T[5296:5297] = 2*bins[-4]-T[5296:5297] # Ambiguous.
T[5297:5299] = 2*bins[-5]-T[5297:5299]
T[5299:5303] = 2*bins[-6]-T[5299:5303]
T[5303:5310] = 2*bins[-7]-T[5303:5310]
T[5310:5327] = 2*bins[-8]-T[5310:5327]
T[5327:5364] = 2*bins[-9]-T[5327:5364]
T[5364:5569] = 2*bins[0]-T[5364:5569]
T[5569:5605] = 2*bins[1]-T[5569:5605]
T[5605:5619] = 2*bins[2]-T[5605:5619]
T[5619:5628] = 2*bins[3]-T[5619:5628]
T[5628:5635] = 2*bins[4]-T[5628:5635]
T[5635:5638] = 2*bins[5]-T[5635:5638]
T[5638:5639] = 2*bins[6]-T[5638:5639] # Ambiguous.
T[5639:5640] = 2*bins[8]-T[5639:5640] # Ambiguous.
T[5640:6056] = T[5640:6056] # >0
T[5641:6057] = T[5641:6057] # Ambiguous.
T[5642:6058] = T[5642:6058] # Ambiguous.
T[6058:6060] = 2*bins[-5]-T[6058:6060]
T[6060:6065] = 2*bins[-6]-T[6060:6065]
T[6065:6071] = 2*bins[-7]-T[6065:6071]
T[6071:6085] = 2*bins[-8]-T[6071:6085]
T[6085:6120] = 2*bins[-9]-T[6085:6120]
T[6120:6327] = 2*bins[0]-T[6120:6327]
T[6327:6355] = 2*bins[1]-T[6327:6355]
T[6355:6371] = 2*bins[2]-T[6355:6371]
T[6371:6381] = 2*bins[3]-T[6371:6381]
T[6381:6385] = 2*bins[4]-T[6381:6385]
T[6385:6388] = 2*bins[5]-T[6385:6388]
T[6388:6390] = 2*bins[6]-T[6388:6390]
T[6390:6391] = 2*bins[7]-T[6390:6391]
T[6391:6392] = 2*bins[8]-T[6391:6392] # Ambiguous.
T[6392:7066] = T[6392:7066] # >0
T[7066:7067] = 2*bins[-3]-T[7066:7067] # Ambiguous.
T[7067:7068] = 2*bins[-4]-T[7067:7068] # Ambiguous.
T[7068:7070] = 2*bins[-5]-T[7068:7070]
T[7070:7074] = 2*bins[-6]-T[7070:7074]
T[7074:7081] = 2*bins[-7]-T[7074:7081]
T[7081:7096] = 2*bins[-8]-T[7081:7096]
T[7096:7132] = 2*bins[-9]-T[7096:7132]
T[7132:7355] = 2*bins[0]-T[7132:7355]
T[7355:7380] = 2*bins[1]-T[7355:7380]
T[7380:7398] = 2*bins[2]-T[7380:7398]
T[7398:7411] = 2*bins[3]-T[7398:7411]
T[7411:7419] = 2*bins[4]-T[7411:7419]
T[7419:7421] = 2*bins[5]-T[7419:7421]
T[7421:7424] = 2*bins[6]-T[7421:7424]
T[7424:7425] = T[7424:7425] # Ambiguous.
T[7425:8154] = T[7425:8154] # >0
T[8154:8155] = 2*bins[-1]-T[8154:8155] # Ambiguous.
T[8155:8156] = 2*bins[-4]-T[8155:8156] # Ambiguous.
T[8156:8158] = 2*bins[-5]-T[8156:8158]
T[8158:8162] = 2*bins[-6]-T[8158:8162]
T[8162:8169] = 2*bins[-7]-T[8162:8169]
T[8169:8186] = 2*bins[-8]-T[8169:8186]
T[8186:8220] = 2*bins[-9]-T[8186:8220]
T[8220:8463] = 2*bins[0]-T[8220:8463]
T[8463:8488] = 2*bins[1]-T[8463:8488]
T[8488:8508] = 2*bins[2]-T[8488:8508]
T[8508:8521] = 2*bins[3]-T[8508:8521]
T[8521:8528] = 2*bins[4]-T[8521:8528]
T[8528:8531] = 2*bins[5]-T[8528:8531]
T[8531:8533] = 2*bins[6]-T[8531:8533]
T[8533:8534] = 2*bins[7]-T[8533:8534]
T[8534:8535] = 2*bins[8]-T[8534:8535] # Ambiguous.
T[8535:8911] = T[8535:8911] # >0


plt.close('all')
plt.figure()
plt.plot(T,'.')
plt.xlim([0,8911])
plt.ylim([-4,5])
plt.xlabel('n')
plt.ylabel('Temp')
plot_rollovers()
