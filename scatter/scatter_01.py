import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
"""
csv_data = pd.read_csv('F:\\Postgraduate_Monk\\Gao\\Gao-2017-07-21\\Fig6_bar_ABC\\python\\mean_dif_py_append.csv')
index_num=['1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12', '13', '14']
data_iloc=csv_data.iloc[:14,1:3]
#df = pd.DataFrame(data_iloc, index=index_num, columns=pd.Index(['Guilty', 'Innocent'], name='peoplestyle'))
df=pd.DataFrame(data_iloc, index=index_num, columns=pd.Index(['bad', 'good'], name='method'))#csv_data.iloc[:14,1]
df.plot(kind='bar')
print(data_iloc)
plt.show()

"""
  #'yellowgreen':          '#9ACD32'}
#'tomato':               '#FF6347',
import numpy as np
import matplotlib.pyplot as plt
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
