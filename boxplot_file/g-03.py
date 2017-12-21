import seaborn as sns
import scipy.io as sio
import os
import os.path as osp

fmat='F:\Postgraduate_Monk\高\高-2017-07-21\python-data\\bad_entropy'

os.listdir(fmat)

sig_name=osp.basename(fmat)
print(sig_name)
# for inname in fmat:
#     print(inname)
#data=sio.loadmat(fmat)


#sns.boxplot(data1, groupby='A','B','C')