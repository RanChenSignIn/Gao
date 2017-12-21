import seaborn as sns
#sns.set()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#the method of bad
sns.set(style="darkgrid")
csv_data = pd.read_csv('.\python\\ly_hon_bad_py.csv')
fig= plt.figure(1,figsize=(6.23,3))
fig.subplots_adjust(left=0.09, bottom=0.13, right=0.99, top=0.94, wspace=0.06, hspace=0.30)
ax=sns.boxplot(x="num", y="data", hue="char", palette="dark",notch=True,data=csv_data,linewidth=1.5)#,orient="h",color=('#FF851B','#FF4136')
#marks
x_position=[0,1,2,9,11,12,13]#np.arange(1,13,1)
y_position=[1.15,1.15,1.15,1.15,1.15,1.15,1.15]
plt.scatter(x_position,y_position,marker = '+', s = 50)#, color = 'r'
plt.ylim(-0.1,1.4)
#axes_add
ax.set_title('The common WE method',fontsize=8)#the title of bad_methods
ax.set_ylabel('$Mean_{WE}^{P3}$',fontsize=8)
ax.set_xlabel('Electrodes',fontsize=8)
elec2=['O2','O1','OZ','PZ','P4','P3','C4','CZ','C3','FZ','F4','F3','FP2','FP1'];
plt.yticks(fontsize=6)
ax.set_xticklabels(elec2,fontsize=6)
plt.legend(title="",loc='upper center',ncol=2,fontsize=6,frameon=False)#, frameon = False  ('Innocent','Guilty','chen','ran'),loc = (.85,.1),
#plt.savefig(".\\bad_method" + '.png', dpi=600)  # +elec2[num-1]  #循环保存图片  bad_method
plt.show()


#the method of good
"""
csv_data = pd.read_csv('.\python\\ly_hon_good_py.csv')
fig= plt.figure(2,figsize=(6.23,3))
fig.subplots_adjust(left=0.09, bottom=0.13, right=0.99, top=0.94, wspace=0.06, hspace=0.30)
ax=sns.boxplot(x="num", y="data", hue="char", palette="dark",notch=True,data=csv_data,linewidth=1.5)#,orient="h",color=('#FF851B','#FF4136')
#marks
x_position=[0,1,2,12,13]#np.arange(1,13,1)
y_position=[1.25,1.25,1.25,1.25,1.25]
plt.scatter(x_position,y_position,marker = '+', s = 80)#, color = 'r'
plt.ylim(-0.1,1.5)
#axes_add
ax.set_title('The improved WE method',fontsize=8)#the title of good_methods
ax.set_ylabel('$Impv_{WE}^{P3}$',fontsize=8)
ax.set_xlabel('Electrodes',fontsize=8)
elec2=['O2','O1','OZ','PZ','P4','P3','C4','CZ','C3','FZ','F4','F3','FP2','FP1'];
plt.yticks(fontsize=6)
colors=[]
ax.set_xticklabels(elec2,fontsize=6)#('Innocent','Guilty'),
plt.legend(title="",loc='upper center',ncol=2,fontsize=6,frameon=False)#, frameon = False  ('Innocent','Guilty','chen','ran'),loc = (.85,.1),
#plt.savefig(".\good_method" + '.png', dpi=600)  # +elec2[num-1]  #循环保存图片  good_method
plt.show()


#the difference of the mean of bad and good,
# path='F:\\Postgraduate_Monk\\Gao\\Gao-2017-07-21\\Fig6_bar_ABC\\'
csv_data = pd.read_csv('.\python\\mean_dif_py_err.csv')
fig= plt.figure(3,figsize=(6.23,3))
ax=fig.add_subplot(111)
ax=fig.subplots_adjust(left=0.09, bottom=0.13, right=0.99, top=0.94, wspace=0.06, hspace=0.30)
bad_mean=csv_data.iloc[:14,1]
good_mean=csv_data.iloc[14:28,1]
i_cal_err=csv_data.iloc[14:28,3]
m=0.3
print(i_cal_err)
x=np.arange(14)+1
#ax.xaxis.grid(True, which='major') #x坐标轴的网格使用主刻度
#plt.grid( color='k',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
plt.bar(x,bad_mean,width=m,color="#FF851B",linewidth=1.3,yerr=i_cal_err)#yellowgreen  tomato
plt.bar(x+m,good_mean,width=m,color="#55A868",linewidth=1.3)##FF851B", "#55A868
#plt.bar(x+m,i_cal_err,width=m,color="#55A868",linewidth=1.3)##FF851B", "#55A868

plt.legend(['The common WE method','The improved WE method'],fontsize=6, loc='upper right',frameon=False)
plt.plot([1,14],[0,0],linestyle='--',linewidth=1.0,color='k')
plt.title('The comparison of the difference of mean',fontsize=8)
plt.ylabel('Difference of mean',fontsize=8)
plt.xlabel('Electrodes',fontsize=8)

plt.xlim(0,15.8)
plt.yticks(fontsize=6)
elec2=['O2','O1','OZ','PZ','P4','P3','C4','CZ','C3','FZ','F4','F3','FP2','FP1']
xtick_x=x+m+0.04
plt.xticks(xtick_x,elec2,fontsize=6)#('Innocent','Guilty'),,fontproperties='Times New Roman'
plt.savefig(".\mean_diff" + '.png', dpi=600)  # +elec2[num-1]  #循环保存图片  good_method
plt.show()
"""