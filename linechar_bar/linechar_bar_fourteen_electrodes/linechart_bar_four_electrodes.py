#the first code of four electrodes
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import scipy.io as sio
from matplotlib.font_manager import FontProperties

path='.\python'
path_hon_1='\entropy_hon1.mat'
path_hon_2='\entropy_hon2.mat'
path_hon_3='\entropy_hon3.mat'
path_hon_4='\entropy_hon4.mat'
path_ly_1='\entropy_ly1.mat'
path_ly_2='\entropy_ly2.mat'
path_ly_3='\entropy_ly3.mat'
path_ly_4='\entropy_ly4.mat'
##############################################################
font = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\msyhbd.ttf", size=6)
#OZ
fig_OZ= plt.figure(1,figsize=(3.67,1.37))
fig_OZ.subplots_adjust(left=0.0, bottom=0.3, right=0.99, top=0.9, wspace=0.1, hspace=0.3)
#ax1 = fig_OZ.add_subplot(121)
ax1= fig_OZ.add_axes([0.1, 0.18,0.61,0.75])  # [left, bottom, width, height]
#hon
x=np.linspace(1,15,4)
data_hon_1=sio.loadmat(path+path_hon_1)
Swt_hon = data_hon_1['Swt']
Swt_hon=Swt_hon.T
ax1.plot(x,Swt_hon,linestyle='-',color="#55A868",marker='o',linewidth=4)
#ly
data_ly_1=sio.loadmat(path+path_ly_1)
Swt_ly = data_ly_1['Swt']
Swt_ly=Swt_ly.T
ax1.plot(x,Swt_ly, linestyle='-', color="#FF851B", marker='s', linewidth=4)
#set add  x_label ticks

plt.legend(('Innocent','Guilty'),loc='upper right',ncol=1,fontsize=6,frameon = False)#,bbox_to_anchor=(10,0.5)
ax1.set_ylabel('Time_varying WE',fontproperties=font)
#ax1.set_xlabel('Time window',fontproperties=font)#Electrode Position
ax1.text(5,-0.25,'Time window',fontproperties=font)
#ax1.set_title('OZ',fontsize=12)
#ax1.text(10,1.2,'OZ',fontsize=10)
plt.yticks(fontsize=6)
elec2 = ('10', '11', '12', '13')#,'bad', 'good')
plt.xticks([1, (14*1/3)+1, (14*2/3)+1, (14*3/3)+1], elec2, fontproperties='Times New Roman', fontsize=6)
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
ax1.set_xlim(0, 16)
ax1.set_ylim(0,1.2)
# plt.show()
#add the bar of innocent and guilty of bad and good
# the method of bad and good of hon
ax2= fig_OZ.add_axes([0.795, 0.18,0.2,0.75])  # [left, bottom, width, height]
width =1
ind=np.arange(6)
ax2.set_xlim(0,7)
ax2.set_ylim(0,1.2)
data_hon_1=sio.loadmat(path+path_hon_1)
data_ly_1=sio.loadmat(path+path_ly_1)
hon_ave_bad=data_hon_1['entropy_hon_ave_bad']
hon_ave_bad=hon_ave_bad.T
rects1 = ax2.bar(ind[1], hon_ave_bad, width, color="#55A868",ecolor="#55A868",linewidth=1.5)
ly_ave_bad=data_ly_1['entropy_lying_ave_bad']
ly_ave_bad=ly_ave_bad.T
rects3 = ax2.bar(ind[2], ly_ave_bad, width, color="#FF851B",ecolor="#FF851B",linewidth=1.5)
plt.legend(('Innocent','Guilty'),loc='upper right',ncol=1,fontsize=4,frameon=False)#bbox_to_anchor=(1.4,0.0)
# the method of bad and good of ly
hon_ave_good=data_hon_1['entropy_hon_ave_good']
hon_ave_good=hon_ave_good.T
rects2 = ax2.bar(ind[4], hon_ave_good, width,color="#55A868",ecolor="#55A868",linewidth=1.5)
ly_ave_good=data_ly_1['entropy_lying_ave_good']
ly_ave_good=ly_ave_good.T
rects4 = ax2.bar(ind[5], ly_ave_good, width,color="#FF851B",linewidth=1.5)
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.yaxis.set_ticks_position('left')
#ax2.set_ylabel('W', fontsize=8)
ax2.text(3.8, -0.105,'$Impv_{WE}^{P3}$',fontproperties=font)
ax2.text(0.7,-0.105,'$Mean_{WE}^{P3}$',fontproperties=font)
ax2.text(1.4,-0.255,'WE method',fontproperties=font)
plt.yticks(fontsize=6)
plt.ylabel('WE',fontproperties=font)
plt.xticks([])
ax2.xaxis.set_ticks_position('bottom')
fig_OZ.savefig('.\png_figure\\fig_OZ.png', dpi=600)
# plt.show()
#####################################################################
#PZ
fig_PZ= plt.figure(2,figsize=(3.67,1.37))
fig_PZ.subplots_adjust(left=0.0, bottom=0.3, right=0.99, top=0.9, wspace=0.1, hspace=0.3)
#ax1 = fig_PZ.add_subplot(121)
ax1= fig_PZ.add_axes([0.1, 0.18,0.61,0.75])  # [left, bottom, width, height]
#hon
x=np.linspace(1,15,4)
data_hon_2=sio.loadmat(path+path_hon_2)
Swt_hon = data_hon_2['Swt']
Swt_hon=Swt_hon.T
ax1.plot(x,Swt_hon,linestyle='-',color="#55A868",marker='o',linewidth=4)
#ly
data_ly_2=sio.loadmat(path+path_ly_2)
Swt_ly = data_ly_2['Swt']
Swt_ly=Swt_ly.T
ax1.plot(x,Swt_ly, linestyle='-', color="#FF851B", marker='s', linewidth=4)
#set add  x_label ticks
plt.legend(('Innocent','Guilty'),loc='upper right',ncol=1,fontsize=6,frameon = False)#,bbox_to_anchor=(10,0.5)
ax1.set_ylabel('Time_varying WE',fontproperties=font)
#ax1.set_xlabel('Time window',fontproperties=font)#Electrode Position
ax1.text(5,-0.168,'Time window',fontproperties=font)
plt.yticks(fontsize=6)
elec2 = ('10', '11', '12', '13')#,'bad', 'good')
plt.xticks([1, (14*1/3)+1, (14*2/3)+1, (14*3/3)+1], elec2, fontproperties='Times New Roman', fontsize=6)
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
ax1.set_xlim(0, 16)
ax1.set_ylim(0,0.8)
# plt.show()
#add the bar of innocent and guilty of bad and good
# the method of bad and good of hon
ax2= fig_PZ.add_axes([0.795, 0.18,0.2,0.75])  # [left, bottom, width, height]
width =1
ind=np.arange(6)
ax2.set_xlim(0,7)
ax2.set_ylim(0,0.8)
data_hon_2=sio.loadmat(path+path_hon_2)
data_ly_2=sio.loadmat(path+path_ly_2)
hon_ave_bad=data_hon_2['entropy_hon_ave_bad']
hon_ave_bad=hon_ave_bad.T
rects1 = ax2.bar(ind[1], hon_ave_bad, width, color="#55A868",ecolor="#55A868",linewidth=1.5)
ly_ave_bad=data_ly_2['entropy_lying_ave_bad']
ly_ave_bad=ly_ave_bad.T
rects3 = ax2.bar(ind[2], ly_ave_bad, width, color="#FF851B",ecolor="#FF851B",linewidth=1.5)
plt.legend(('Innocent','Guilty'),loc='upper right',ncol=1,fontsize=4,frameon=False)#bbox_to_anchor=(1.4,0.0)
# the method of bad and good of ly
hon_ave_good=data_hon_2['entropy_hon_ave_good']
hon_ave_good=hon_ave_good.T
rects2 = ax2.bar(ind[4], hon_ave_good, width,color="#55A868",ecolor="#55A868",linewidth=1.5)
ly_ave_good=data_ly_2['entropy_lying_ave_good']
ly_ave_good=ly_ave_good.T
rects4 = ax2.bar(ind[5], ly_ave_good, width,color="#FF851B",linewidth=1.5)
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.yaxis.set_ticks_position('left')
ax2.text(3.8, -0.07,'$Impv_{WE}^{P3}$',fontproperties=font)
ax2.text(0.7,-0.07,'$Mean_{WE}^{P3}$',fontproperties=font)
ax2.text(1.4,-0.17,'WE method',fontproperties=font)
ax2.yaxis.set_ticks_position('left')
plt.yticks(fontsize=6)
plt.xticks([])
plt.ylabel('WE',fontproperties=font)
ax2.xaxis.set_ticks_position('bottom')
fig_PZ.savefig('.\png_figure\\fig_PZ.png', dpi=600)
# plt.show()
###################################################################################
#CZ
fig_CZ= plt.figure(3,figsize=(3.67,1.37))
fig_CZ.subplots_adjust(left=0.0, bottom=0.3, right=0.99, top=0.9, wspace=0.1, hspace=0.3)
#ax1 = fig_CZ.add_subplot(121)
ax1= fig_CZ.add_axes([0.1, 0.18,0.61,0.75])  # [left, bottom, width, height]
#hon
x=np.linspace(1,15,4)
data_hon_3=sio.loadmat(path+path_hon_3)
Swt_hon = data_hon_3['Swt']
Swt_hon=Swt_hon.T
ax1.plot(x,Swt_hon,linestyle='-',color="#55A868",marker='o',linewidth=4)
#ly
data_ly_3=sio.loadmat(path+path_ly_3)
Swt_ly = data_ly_3['Swt']
Swt_ly=Swt_ly.T
ax1.plot(x,Swt_ly, linestyle='-', color="#FF851B", marker='s', linewidth=4)
#set add  x_label ticks
plt.legend(('Innocent','Guilty'),loc='upper right',ncol=1,fontsize=6,frameon = False)#,bbox_to_anchor=(10,0.5)
ax1.set_ylabel('Time_varying WE',fontproperties=font)
#ax1.set_xlabel('Time window',fontproperties=font)#Electrode Position
ax1.text(5,-0.25,'Time window',fontproperties=font)
plt.yticks(fontsize=6)
elec2 = ( '10', '11', '12', '13')#,'bad', 'good')
plt.xticks([1, (14*1/3)+1, (14*2/3)+1, (14*3/3)+1], elec2, fontproperties='Times New Roman', fontsize=6)
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
ax1.set_xlim(0, 16)
ax1.set_ylim(0,1.2)
# plt.show()
#add the bar of innocent and guilty of bad and good
# the method of bad and good of hon
ax2= fig_CZ.add_axes([0.795, 0.18,0.2,0.75])  # [left, bottom, width, height]
width =1
ind=np.arange(6)
ax2.set_xlim(0,7)
ax2.set_ylim(0,1.2)
data_hon_3=sio.loadmat(path+path_hon_3)
data_ly_3=sio.loadmat(path+path_ly_3)
hon_ave_bad=data_hon_3['entropy_hon_ave_bad']
hon_ave_bad=hon_ave_bad.T
rects1 = ax2.bar(ind[1], hon_ave_bad, width, color="#55A868",ecolor="#55A868",linewidth=1.5)
ly_ave_bad=data_ly_3['entropy_lying_ave_bad']
ly_ave_bad=ly_ave_bad.T
rects3 = ax2.bar(ind[2], ly_ave_bad, width, color="#FF851B",ecolor="#FF851B",linewidth=1.5)
plt.legend(('Innocent','Guilty'),loc='upper right',ncol=1,fontsize=4,frameon=False)#bbox_to_anchor=(1.4,0.0)
# the method of bad and good of ly
hon_ave_good=data_hon_3['entropy_hon_ave_good']
hon_ave_good=hon_ave_good.T
rects2 = ax2.bar(ind[4], hon_ave_good, width,color="#55A868",ecolor="#55A868",linewidth=1.5)
ly_ave_good=data_ly_3['entropy_lying_ave_good']
ly_ave_good=ly_ave_good.T
rects4 = ax2.bar(ind[5], ly_ave_good, width,color="#FF851B",linewidth=1.5)
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.yaxis.set_ticks_position('left')
ax2.text(3.8, -0.105,'$Impv_{WE}^{P3}$',fontproperties=font)
ax2.text(0.7,-0.105,'$Mean_{WE}^{P3}$',fontproperties=font)
ax2.text(1.4,-0.255,'WE method',fontproperties=font)
ax2.yaxis.set_ticks_position('left')
plt.yticks(fontsize=6)
plt.xticks([])
plt.ylabel('WE',fontproperties=font)
ax2.xaxis.set_ticks_position('bottom')
fig_CZ.savefig('.\png_figure\\fig_CZ.png', dpi=600)
# plt.show()
################################################################################################
#FZ
fig_FZ= plt.figure(4,figsize=(3.67,1.37))
fig_FZ.subplots_adjust(left=0.0, bottom=0.3, right=0.99, top=0.9, wspace=0.1, hspace=0.3)
#ax1 = fig_FZ.add_subplot(121)
ax1= fig_FZ.add_axes([0.1, 0.18,0.61,0.75])  # [left, bottom, width, height]
#hon
x=np.linspace(1,15,4)
data_hon_4=sio.loadmat(path+path_hon_4)
Swt_hon = data_hon_4['Swt']
Swt_hon=Swt_hon.T
ax1.plot(x,Swt_hon,linestyle='-',color="#55A868",marker='o',linewidth=4)
#ly
data_ly_4=sio.loadmat(path+path_ly_4)
Swt_ly = data_ly_4['Swt']
Swt_ly=Swt_ly.T
ax1.plot(x,Swt_ly, linestyle='-', color="#FF851B", marker='s', linewidth=4)
#set add  x_label ticks
plt.legend(('Innocent','Guilty'),loc='upper right',ncol=1,fontsize=6,frameon = False)#,bbox_to_anchor=(10,0.5)
ax1.set_ylabel('Time_varying WE',fontproperties=font)
#ax1.set_xlabel('Time window',fontproperties=font)#Electrode Position
ax1.text(5,-0.25,'Time window',fontproperties=font)
plt.yticks(fontsize=6)
elec2 = ( '10', '11', '12', '13')#,'bad', 'good')
plt.xticks([1, (14*1/3)+1, (14*2/3)+1, (14*3/3)+1], elec2, fontproperties='Times New Roman', fontsize=6)
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
ax1.set_xlim(0, 16)
ax1.set_ylim(0,1.2)
# plt.show()
#add the bar of innocent and guilty of bad and good
# the method of bad and good of hon
ax2= fig_FZ.add_axes([0.795, 0.18,0.2,0.75])  # [left, bottom, width, height]
width =1
ind=np.arange(6)
ax2.set_xlim(0,7)
ax2.set_ylim(0,1.2)
data_hon_4=sio.loadmat(path+path_hon_4)
data_ly_4=sio.loadmat(path+path_ly_4)
hon_ave_bad=data_hon_4['entropy_hon_ave_bad']
hon_ave_bad=hon_ave_bad.T
rects1 = ax2.bar(ind[1], hon_ave_bad, width, color="#55A868",ecolor="#55A868",linewidth=1.5)
ly_ave_bad=data_ly_4['entropy_lying_ave_bad']
ly_ave_bad=ly_ave_bad.T
rects3 = ax2.bar(ind[2], ly_ave_bad, width, color="#FF851B",ecolor="#FF851B",linewidth=1.5)
plt.legend(('Innocent','Guilty'),loc='upper right',ncol=1,fontsize=4,frameon=False)#bbox_to_anchor=(1.4,0.0)
# the method of bad and good of ly
hon_ave_good=data_hon_4['entropy_hon_ave_good']
hon_ave_good=hon_ave_good.T
rects2 = ax2.bar(ind[4], hon_ave_good, width,color="#55A868",ecolor="#55A868",linewidth=1.5)
ly_ave_good=data_ly_4['entropy_lying_ave_good']
ly_ave_good=ly_ave_good.T
rects4 = ax2.bar(ind[5], ly_ave_good, width,color="#FF851B",linewidth=1.5)
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.yaxis.set_ticks_position('left')
ax2.text(3.8, -0.105,'$Impv_{WE}^{P3}$',fontproperties=font)
ax2.text(0.7,-0.105,'$Mean_{WE}^{P3}$',fontproperties=font)
ax2.text(1.4,-0.255,'WE method',fontproperties=font)
ax2.yaxis.set_ticks_position('left')
plt.yticks(fontsize=6)
plt.xticks([])
plt.ylabel('WE',fontproperties=font)
ax2.xaxis.set_ticks_position('bottom')
fig_FZ.savefig('.\png_figure\\fig_FZ.png', dpi=600)
"""
#########################################################################################################
#the sceond code of fourteen electrodes
