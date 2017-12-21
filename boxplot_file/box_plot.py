import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#creat data
np.random.seed(10)
collectn_1=np.random.normal(100,10,200)
collectn_2=np.random.normal(80,30,200)
collectn_3=np.random.normal(90,20,200)
collectn_4=np.random.normal(70,25,200)

#combine all collections into a list
data_to_plot=[collectn_1,collectn_2,collectn_3,collectn_4]

#create a figure instance
fig=plt.figure(1,figsize=(9,6))

#create an axes instance
ax=fig.add_subplot(111)

#create a boxplot
#bp=ax.boxplot(data_to_plot)#one
bp=ax.boxplot(data_to_plot,patch_artist=True,)#two

#change outline color ,fill color and linewidth of the boxes
for box in bp['boxes']:
    #change outline color
    box.set(color='#FF851B',linewidth=2)
    #change fill color
    box.set(facecolor='#FF851B')

#change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3',linewidth=2)

#change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color='#7570b3',linewidth=2)

#change color and linewidth of the medians
for median in bp['medians']:
    median.set(color='#b2df8a',linewidth=2)

#change the style of fliers and their fill
for flier in bp['fliers']:
    flier.set(marker='*',color='#e7298a',alpha=0.5)

#custom x-axis labels
ax.set_xticklabels(['samples1','samples2','samples3','samples4'])

#remove top axes and right axes ticks
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.show(fig)
