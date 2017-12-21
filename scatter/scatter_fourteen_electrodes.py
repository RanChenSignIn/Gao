import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import scipy.io as sio
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\\WINDOWS\\Fonts\\msyhbd.ttf")


for i in range(1,15):#大循环1-14个电极，先绘制前七个电极，后绘制后七个电极
    # 前七个电极的common method and improve method

    if i<=7:
        fig = plt.figure(1, figsize=(7, 9.84))
        fig.subplots_adjust(left=0.05, bottom=0.055, right=0.98, top=0.975, wspace=0.13, hspace=0.09)
        #the common method
        path = './python/Common_method'
        data_common=sio.loadmat(path+'/mean'+str(i)+'.mat')
        mean_hon=data_common['mean_hon'].T
        mean_hon_ave=data_common['mean_hon_ave'].T
        mean_lying=data_common['mean_lying'].T
        mean_lying_ave=data_common['mean_lying_ave'].T

        x_num=np.arange(1,16,1)
        ax1=fig.add_subplot(7,2,2*i-1)
        ax1.scatter(x_num,mean_hon,color="#DAA520", s=35, marker='H')#DAA520  FF0000
        if i==1:
            ax1.set_yticks([0.4,0.6,0.8])
            ax1.set_ylim(0.1, 0.95)
        elif i in[2,3]:
            ax1.set_ylim(0.1, 0.95)
            ax1.set_yticks([0.2,0.4,0.6,0.8])
        else:
            ax1.set_ylim(0.0, 0.7)
            ax1.set_yticks([0.2,0.4,0.6])
        #判断最大值与最小值的范围
        # ax1.set_ylim(mean_min,mean_max)
        ax1.scatter(x_num,mean_lying,color="#FF0000", s=35, marker='H')
        ax1.axhline(y=mean_hon_ave, xmin=0, xmax=15, linewidth=1.5, color='#DAA520')
        ax1.axhline(y=mean_lying_ave, xmin=0, xmax=15, linewidth=1.5, color='#FF0000')
        if i==7:
            plt.text(5, -0.2, 'Subject number', fontproperties=font,fontsize=10)
            #plt.xlabel('Subject number',fontproperties=font,)
            plt.xticks([0,2,4,6,8,10,12,14,16])
        else:
            plt.xticks([])
        if i==1:
            plt.title('$Mean_{WE}^{P3}$',fontproperties=font,fontsize=13)
        #Improve method
        path = './python/Improve_method'
        data_common = sio.loadmat(path + '/mean' + str(i) + '.mat')
        mean_hon = data_common['mean_hon'].T
        mean_hon_ave=data_common['mean_hon_ave'].T
        mean_lying = data_common['mean_lying'].T
        mean_lying_ave=data_common['mean_lying_ave'].T
        x_num = np.arange(1, 16, 1)
        ax2 = fig.add_subplot(7, 2, 2 * i )
        ax2.scatter(x_num, mean_hon, color="#DAA520", s=35 ,marker='H')
        ax2.scatter(x_num, mean_lying, color="#FF0000", s=35, marker='H')
        ax2.axhline(y=mean_hon_ave, xmin=0, xmax=15, linewidth=1.5, color='#DAA520')
        ax2.axhline(y=mean_lying_ave, xmin=0, xmax=15, linewidth=1.5, color='#FF0000')
        if i==7:
            plt.text(5, -0.23, 'Subject number', fontproperties=font,fontsize=10)
            #plt.xlabel('Subject number',fontproperties=font,fontsize=10)
            plt.xticks([0,2,4,6,8,10,12,14,16])
            legend_char = ["group mean of innocent", "group mean of guilty", "mean of one innocent","mean of one guilty"]
            plt.legend(legend_char, loc=(0.0, 0.0), ncol=4, frameon=False, title="", bbox_to_anchor=(-1.21, -0.47),
                       fontsize=7, labelspacing=0.0, handlelength=4)
        else:
            plt.xticks([])
        if i in[1,2,3]:
            ax2.set_yticks([0.2,0.4,0.6,0.8,1.0])
            ax2.set_ylim(0.1,0.95)
        else:
            ax2.set_ylim(0.0,0.7)
            ax2.set_yticks([0.2,0.4,0.6,0.8])
        if i==1:
            plt.title('$Impv_{WE}^{P3}$',fontproperties=font,fontsize=13)
    plt.savefig(".\png_figure\electrodes_fourteen_01" + '.png',dpi=600)

# 后七个电极的common method and improve method
    """
    if i>7:
        fig = plt.figure(2, figsize=(7, 9.8))
        fig.subplots_adjust(left=0.05, bottom=0.055, right=0.98, top=0.975, wspace=0.13, hspace=0.09)
        #the common method
        path = './python/Common_method'
        data_common=sio.loadmat(path+'/mean'+str(i)+'.mat')
        mean_hon=data_common['mean_hon'].T
        mean_hon_ave=data_common['mean_hon_ave'].T
        mean_lying=data_common['mean_lying'].T
        mean_lying_ave=data_common['mean_lying_ave'].T

        x_num=np.arange(1,16,1)
        ax1=fig.add_subplot(7,2,2*(i-7)-1)
        ax1.scatter(x_num,mean_hon,color="#DAA520", s=35, marker='H')#,alpha=0.6
        #设定y轴的范围
        if i in [8,9,10,11,12]:
            ax1.set_yticks([0.2,0.4,0.6])
            ax1.set_ylim(0.0, 0.7)
        else:
            ax1.set_ylim(0.2, 0.95)
            ax1.set_yticks([0.2,0.4,0.6,0.8])
        ax1.scatter(x_num,mean_lying,color="#FF0000", s=35, marker='H')#,alpha=0.6
        ax1.axhline(y=mean_hon_ave, xmin=0, xmax=15, linewidth=1.5, color='#DAA520')
        ax1.axhline(y=mean_lying_ave, xmin=0, xmax=15, linewidth=1.5, color='#FF0000')
        if i==14:
            plt.text(5, -0.02, 'Subject number', fontproperties=font, fontsize=10)
            #plt.xlabel('Subject number',fontproperties=font,fontsize=10)
            plt.xticks([0,2,4,6,8,10,12,14,16])
        else:
            plt.xticks([])
        if i==8:
            plt.title('$Mean_{WE}^{P3}$',fontproperties=font,fontsize=13)
        #Improve method
        path = './python/Improve_method'
        data_common = sio.loadmat(path + '/mean' + str(i) + '.mat')
        mean_hon = data_common['mean_hon'].T
        mean_hon_ave=data_common['mean_hon_ave'].T
        mean_lying = data_common['mean_lying'].T
        mean_lying_ave=data_common['mean_lying_ave'].T
        x_num = np.arange(1, 16, 1)
        ax2 = fig.add_subplot(7, 2, 2 * (i-7) )
        ax2.scatter(x_num, mean_hon, color="#DAA520", s=35 ,marker='H')
        ax2.scatter(x_num, mean_lying, color="#FF0000", s=35, marker='H')
        ax2.axhline(y=mean_hon_ave, xmin=0, xmax=15, linewidth=1.5, color='#DAA520')
        ax2.axhline(y=mean_lying_ave, xmin=0, xmax=15, linewidth=1.5, color='#FF0000')
        if i==14:
            plt.text(5, -0.02, 'Subject number', fontproperties=font,fontsize=10)
            #plt.xlabel('Subject number',fontproperties=font,fontsize=10)
            plt.xticks([0,2,4,6,8,10,12,14,16])
            legend_char = ["group mean of innocent", "group mean of guilty", "mean of one innocent",
                           "mean of one guilty"]
            plt.legend(legend_char, loc=(0.0, 0.0), ncol=4, frameon=False, title="", bbox_to_anchor=(-1.21, -0.47),
                       fontsize=7, labelspacing=0.0, handlelength=4)
        else:
            plt.xticks([])
        #设定y轴的范围
        if i in [8,9,10,11,12]:
            ax2.set_yticks([0.2,0.4,0.6])
            ax2.set_ylim(0.0, 0.7)
        else:
            ax2.set_ylim(0.2, 0.95)
            ax2.set_yticks([0.2,0.4,0.6,0.8])
        if i==8:
            plt.title('$Impv_{WE}^{P3}$',fontproperties=font,fontsize=13)
    plt.savefig(".\png_figure\electrodes_fourteen_02" + '.png',dpi=600)
"""
# plt.show()

    # print(data_common.shape())