import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif']=['SimHei']
filepath = r'I:\Data\Personal Data\graduation project\SACOL\microwave\2007\200705\2007-05-19_19-16-32_lv2.csv'
data = pd.read_csv(filepath)
parameter = 11
a = data.loc[data['10']==parameter]
Del_columns = data.columns[2:10]
a.drop(Del_columns,axis=1,inplace=True)
a.drop('Record',axis=1,inplace=True)
z = a.iloc[:,1:48].T
fig=plt.figure(figsize=(5,4),dpi=1000,frameon=True)
ax=fig.add_axes([0,0,4,2])
ax.set_xlabel('Times')
ax.set_ylabel('Height')
ca=ax.contourf(z,10,cmap="jet")
plt.colorbar(ca)
xla = a.iloc[:,0:1]
xla1 = xla['Date/Time'].apply(lambda x:x[:11]).tolist()
x_ticks = [0]
x_labels = [xla.iloc[0:1,0:1].values]
i = 1
Len = len(xla1)
while i<Len-1:
    if xla1[i-1]!=xla1[i]:
        x_ticks.append(i)
        x_labels.append(xla.iloc[i:i+1,0:1].values)
    i += 1
x_ticks.append(Len-1)
x_labels.append(xla.iloc[Len-1:Len,0:1].values)
plt.xticks(x_ticks,x_labels,fontsize=10)
y_ticks = [0,2,4,6,8,10,14,18,22,26,30,34,38,42,46]
y_labels = ['0','0.2','0.4','0.6','0.8','1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0']
plt.yticks(y_ticks,y_labels,fontsize=9)
#plt.legend()
plt.show()