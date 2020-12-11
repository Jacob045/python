#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   draw_photo_module.py
@Time    :   2020/12/11 11:28:13
@Author  :   Gao Shuoyuan
@Version :   1.0
@Contact :   jacob045@foxmail.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------------------------------------------
# 功能说明：
# 将得到的数据绘制成横坐标为时间，纵坐标为海拔高度，用颜色的变化来表示物理量变化的
# 大气垂直剖面图
# ---------------------------------------------------------------------------------------
# z_data存放图像信息
# a_data存放图像信息+坐标轴信息， z_data和a_data是同源的
# photo存放生成图片的名字
def draw_profile_photo(z_data,a_data,photo):
    fig=plt.figure(figsize=(5,4),dpi=500,frameon=True)
    ax=fig.add_axes([0,0,9,2])
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
    plt.xticks(x_ticks,x_labels,fontsize=12,rotation=45)

    #坐标轴信息——Y轴（设定信息并绘制）
    y_ticks = [0,2,4,6,8,10,14,18,22,26,30,34,38,42,46]
    y_labels = ['0','0.2','0.4','0.6','0.8','1.0','2.0','3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0']
    plt.yticks(y_ticks,y_labels,fontsize=12)
    #-------------------------------------------------------------------------------------
    #生成图片
    plt.savefig(photo,bbox_inches = 'tight')
    #展示图片
    plt.show()


def draw_Linechart_photo(data,photoname):
    plt.rcParams['figure.figsize'] = (10.0,20.0)
    #纵轴上分布高度数值
    Height = data.columns.values[1:48]
    # 绘图
    Len = len(data['Time'])
    i = 0
    while i<Len:
        data_for_print = np.array(data.iloc[i:i+1,1:48]).T
        plt.plot(data_for_print, Height, label=data['Time'][i:i+1].values)
        i = i+1
    #设置X轴
    x_ticks = np.linspace(180, 320, 8)
    plt.xticks(x_ticks,rotation=45)
    # 启动图例
    plt.legend()
    # 添加网格
    plt.grid()
    # 主标题
    plt.title(photoname,fontsize=20,fontweight='bold')
    # 保存图片
    photopath = 'G:/python/work for graduation/photo/' + photoname + '.png'
    plt.savefig(photopath,bbox_inches = 'tight')
    # 展示图片
    plt.show()