import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import scipy.io as sio
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\msyhbd.ttf", size=6)

path='.\python'
for num in range(1,15):
    fig = plt.figure(num, figsize=(3.67, 1.37))
    ax1 = fig.add_axes([0.1, 0.18, 0.61, 0.75])  # [left, bottom, width, height]
    #hon
    x = np.linspace(1, 15, 4)
    path_hon=path+'\entropy_hon'+str(num)+'.mat'
    data_hon=sio.loadmat(path_hon)
    Swt_hon = data_hon['Swt']
    Swt_hon = Swt_hon.T
    plt.plot(x, Swt_hon, linestyle='-', color="#55A868", marker='o', linewidth=4)
    # ly
    path_ly=path+'\entropy_ly'+str(num)+'.mat'
    data_ly = sio.loadmat(path_ly)
    Swt_ly = data_ly['Swt']
    Swt_ly = Swt_ly.T
    plt.plot(x, Swt_ly, linestyle='-', color="#FF851B", marker='s', linewidth=4)
    ax1.set_xlim(0, 16)
    if num in [1, 7, 12, 14]:
        ax1.set_ylim(0, 1.6)
    else:
        ax1.set_ylim(0, 1.4)
    plt.legend(('Innocent', 'Guilty'), loc='upper center', ncol=1, fontsize=6, frameon=False)  # ,bbox_to_anchor=(10,0.5)
    ax1.set_ylabel('Time_varying WE', fontproperties=font)
    # ax1.set_xlabel('Time window',fontproperties=font)#Electrode Position
    ax1.text(5, -0.27, 'Time window', fontproperties=font)
    #ax1.set_xlabel('Time window', fontproperties=font)
    plt.yticks(fontsize=6)
    elec2 = ('10', '11', '12', '13')  # ,'bad', 'good')
    plt.xticks([1, (14 * 1 / 3) + 1, (14 * 2 / 3) + 1, (14 * 3 / 3) + 1], elec2, fontproperties='Times New Roman',
               fontsize=6)
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.yaxis.set_ticks_position('left')
    ax1.xaxis.set_ticks_position('bottom')

    #
    ax2 = fig.add_axes([0.795, 0.18, 0.2, 0.75])  # [left, bottom, width, height]
    width = 1
    ind = np.arange(6)
    ax2.set_xlim(0, 7)
    ax2.set_ylim(0, 1.4)
    data_hon = sio.loadmat(path_hon)
    data_ly = sio.loadmat(path_ly)
    hon_ave_bad = data_hon['entropy_hon_ave_bad']
    hon_ave_bad = hon_ave_bad.T
    rects1 = ax2.bar(ind[1], hon_ave_bad, width, color="#55A868", ecolor="#55A868", linewidth=1.5)
    ly_ave_bad = data_ly['entropy_lying_ave_bad']
    ly_ave_bad = ly_ave_bad.T
    rects3 = ax2.bar(ind[2], ly_ave_bad, width, color="#FF851B", ecolor="#FF851B", linewidth=1.5)
    plt.legend(('Innocent', 'Guilty'), loc='upper center', ncol=1, fontsize=4, frameon=False)  # bbox_to_anchor=(1.4,0.0)
    # the method of bad and good of ly
    hon_ave_good = data_hon['entropy_hon_ave_good']
    hon_ave_good = hon_ave_good.T
    rects2 = ax2.bar(ind[4], hon_ave_good, width, color="#55A868", ecolor="#55A868", linewidth=1.5)
    ly_ave_good = data_ly['entropy_lying_ave_good']
    ly_ave_good = ly_ave_good.T
    rects4 = ax2.bar(ind[5], ly_ave_good, width, color="#FF851B", linewidth=1.5)
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.yaxis.set_ticks_position('left')
    # ax2.set_ylabel('W', fontsize=8)
    ax2.text(3.8, -0.12, '$Impv_{WE}^{P3}$', fontproperties=font)
    ax2.text(0.7, -0.12, '$Mean_{WE}^{P3}$', fontproperties=font)
    ax2.text(1.4, -0.255, 'WE method', fontproperties=font)
    plt.yticks(fontsize=6)
    plt.ylabel('WE', fontproperties=font)
    plt.xticks([])
    ax2.xaxis.set_ticks_position('bottom')
    fig.savefig('.\png_figure\Electrodes_fourteen\\fig'+str(num)+'.png', dpi=600)
#plt.show()
