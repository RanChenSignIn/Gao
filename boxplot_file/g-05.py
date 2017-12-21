import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")

# Load the example tips dataset
tips = sns.load_dataset("tips")
print(tips)
# Draw a nested boxplot to show bills by day and sex
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips, palette="PRGn")
sns.despine(offset=10, trim=True)
plt.show()


"""
fmat2=fmat+'\ly_hon2.mat'
fmat3=fmat+'\ly_hon3.mat'
fmat4=fmat+'\ly_hon4.mat'
fmat5=fmat+'\ly_hon5.mat'
fmat6=fmat+'\ly_hon6.mat'
fmat7=fmat+'\ly_hon7.mat'
fmat8=fmat+'\ly_hon8.mat'
fmat9=fmat+'\ly_hon9.mat'
fmat10=fmat+'\ly_hon10.mat'
fmat11=fmat+'\ly_hon11.mat'
fmat12=fmat+'\ly_hon12.mat'
fmat13=fmat+'\ly_hon13.mat'
fmat14=fmat+'\ly_hon14.mat'

data1 = pd.DataFrame(fmat1).assign(Location=1)
data2 = pd.DataFrame(fmat2).assign(Location=2)
data3 = pd.DataFrame(fmat3).assign(Location=3)
data4 = pd.DataFrame(fmat4).assign(Location=4)
data5 = pd.DataFrame(fmat5).assign(Location=5)
data6 = pd.DataFrame(fmat6).assign(Location=6)
data7 = pd.DataFrame(fmat7).assign(Location=7)
data8 = pd.DataFrame(fmat8).assign(Location=8)
data9 = pd.DataFrame(fmat9).assign(Location=9)
data10 = pd.DataFrame(fmat10).assign(Location=10)
data11= pd.DataFrame(fmat11).assign(Location=11)
data12= pd.DataFrame(fmat12).assign(Location=12)
data13= pd.DataFrame(fmat13).assign(Location=13)
data14= pd.DataFrame(fmat14).assign(Location=14)#, columns=elec2

cdf = pd.concat([data1, data2, data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14])
mdf = pd.melt(cdf, id_vars=['Location'], var_name=['Letter'])
"""