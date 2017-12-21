import seaborn as sns
import os.path
import matplotlib.pyplot as plt
# import csv
import numpy as np
import scipy.io as sio
import pandas as pd

#sns.set_color_codes("dark")
# print(dir(sns))
# sns.set_color_codes("dark")
#
# _ = plt.plot([0, 1], color="#FF4136")
# _ = plt.plot([0, 2], color="#001C7F")
# plt.show()
#
# deep=["#4C72B0", "#55A868", "#C44E52",
#           "#8172B2", "#CCB974", "#64B5CD"],
# """
"""
for whisker in ax['whiskers']:
    whisker.set(color='#7570b3',linewidth=2)





print(csv_data[:3])
for item in csv_data:
    print(item)

elec=[1,2,3,4,5,12,8,15,19,21,22,27,28,30];  #电极代表的序列号
elec2=['O2','O1','OZ','PZ','P4','P3','C4','CZ','C3','FZ','F4','F3','FP2','FP1'];

path='F:\Postgraduate_Monk\高\高-2017-07-21\Fig 6 bar 图ABC\python'
fmat1=path+'\ly_hon_all.xslx'


fmat1_data=sns.load_dataset("fmat1")
fmat1_data=sio.loadmat(fmat1)#,mdict=np.dtype('u4')

sns.boxplot(x="num", y="data", hue="char", data=fmat1_data, orient="h", palette="PRGn")
ax = sns.boxplot(data=mdf, orient="h", palette="Set2")


tips["weekend"] = tips["day"].isin(["Sat", "Sun"])
ax = sns.boxplot(x="day", y="total_bill", hue="weekend",
   ...                 data=tips, dodge=False)
ax = sns.boxplot(x="day", y="total_bill", data=tips)
ax = sns.swarmplot(x="day", y="total_bill", data=tips, color=".25")

"""
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
n_bins = 10
#x = np.random.randn(1000, 3)
fig= plt.figure(4,figsize=(10,8))
ax3= fig.add_axes([0.1, 0.18,0.61,0.75])  # [left, bottom, width, height]
#ax3 = axes.flatten()
#ax0, ax1, ax2,
colors = ['red', 'tan', 'lime']
# ax0.hist(x, n_bins, normed=1, histtype='bar', color=colors, label=colors)
# ax0.legend(prop={'size': 10})
# ax0.set_title('bars with legend')
#
# ax1.hist(x, n_bins, normed=1, histtype='bar', stacked=True)
# ax1.set_title('stacked bar')
#
# ax2.hist(x, n_bins, histtype='step', stacked=True, fill=False)
# ax2.set_title('stack step (unfilled)')
# Make a multiple-histogram of data-sets with different length.
x_multi = [np.random.randn(n) for n in [1, 1, 1]]
ax3.hist(x_multi, n_bins, histtype='bar')
ax3.set_title('different sample sizes')
plt.show()