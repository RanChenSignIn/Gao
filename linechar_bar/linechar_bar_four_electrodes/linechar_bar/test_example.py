import matplotlib.pyplot as plt
import numpy as np
# x=[1,2,3,4]
# y=[4,5,8,10]
# plt.scatter(x,y,s=20)  #scatter绘制点，输入x和y坐标   ,实参s绘制图形中点的尺寸
# plt.show()


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
#matplotlib inline

x=np.array([[0,1,2,3,4,5]])
fig, axes = plt.subplots(2,3,figsize=(20,10))  #这个可以方便同时建立画板画布
axes[0,1].plot(np.random.randn(10))  #第1行第二个画布绘图
axes[0,2].plot(np.random.randn(10),'g--',marker='o')

arr = np.random.randn(20).cumsum()
axes[1,1].plot(np.random.randn(20).cumsum(),linestyle='--',color='red',marker='o')
plt.plot(np.random.randn(20).cumsum(),'k--')  #未给定画布则在最后一个画布上绘图
axes[1,0].plot(arr,linestyle='dashed',color='yellow',marker='*')

data = DataFrame(np.random.randn(2,3),columns=['a','b','c'])
data.plot(ax=axes[0,0])  #针对DataFrame可以使用参数给定画布
plt.show()
#plt.savefig('test.png',dpi=400,bbox_inches='tight',facecolor='m')
#保存到指定路径，dpi-像素，bbox_inches-剪除当前图表周围空白,facecolor-背景颜色


#pl.plot(x,Swt_hon, linestyle'r*--')

#plt.scatter(x, Swt_hon,color='yellow', marker='*')
#plt.plot(x,Swt_hon,'ko',label="--")
#ax.plot(Swt_hon, 'o-',label='All of BUGs')
# t = pd.DataFrame(Swt_hon,index = x)
# t.plot()

# linestyle='dashed',
#plt.scatter(x,Swt_hon)
# ax.barh(y_pos, performance, xerr=error, align='center',
#         color='green', ecolor='black')#水平bar


# class figure_set:
#     def __init__(self,data=None):
#         self.data=data
#     def set_plot(self):