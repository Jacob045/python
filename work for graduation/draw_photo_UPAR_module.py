#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   print_photo_UPAR_module.py
@Time    :   2020/12/10 22:19:06
@Author  :   Gao Shuoyuan
@Version :   1.0
@Contact :   jacob045@foxmail.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import numpy as np
import matplotlib.pyplot as plt

def draw_photo_UPAR(data,photoname):
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
    plt.savefig(photoname,bbox_inches = 'tight')
    # 展示图片
    plt.show()