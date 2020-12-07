#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   print_photo_module.py
@Time    :   2020/12/07 16:44:30
@Author  :   Gao Shuoyuan
@Version :   1.0
@Contact :   jacob045@foxmail.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import matplotlib.pyplot as plt

# z_data存放图像信息
# a_data存放图像信息+坐标轴信息， z_data和a_data是同源的
# photo存放生成图片的名字
def print_photo(z_data,a_data,photo):
    fig=plt.figure(figsize=(5,4),dpi=600,frameon=True)
    ax=fig.add_axes([0,0,7,2])
    ax.set_xlabel('Times',fontsize=20)
    ax.set_ylabel('Height',fontsize=20)
    ca=ax.contourf(z_data,10,cmap="jet")
    #图例信息
    plt.colorbar(ca)
    #坐标轴信息——X轴（设定信息并绘制）
    xla = a_data.iloc[:,0:1]
    xla1 = xla['Date/Time'].apply(lambda x:x[:11]).tolist()
    x_ticks = [0]
    x_labels = [str(xla.iloc[0:1,0:1])[24:42]]
    i = 1
    Len = len(xla1)
    while i<Len-1:
        if xla1[i-1]!=xla1[i]:
            x_ticks.append(i)
            x_labels.append(str(xla.iloc[i:i+1,0:1])[28:45])
        i += 1
    x_ticks.append(Len-1)
    x_labels.append(str(xla.iloc[Len-1:Len,0:1])[30:47])
    plt.xticks(x_ticks,x_labels,fontsize=12)
    #坐标轴信息——Y轴（设定信息并绘制）
    y_ticks = [0,2,4,6,8,10,14,18,22,26,30,34,38,42,46]
    y_labels = ['0','0.2','0.4','0.6','0.8','1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0']
    plt.yticks(y_ticks,y_labels,fontsize=12)
    #生成图片
    plt.savefig(photo,bbox_inches = 'tight')
    #展示图片
    plt.show()