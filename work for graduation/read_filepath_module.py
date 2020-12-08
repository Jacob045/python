#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   read_filepath.py
@Time    :   2020/12/08 20:57:30
@Author  :   Gao Shuoyuan
@Version :   1.0
@Contact :   jacob045@foxmail.com
@License :   (C)Copyright 2020-2021, Liugroup-NLPR-CASIA
@Desc    :   None
'''
# 功能说明
# 从多级嵌套的文件中找到包含特定关键字的的文件，并返回一个包含这些文件路径的数组
# here put the import lib
import os
# Path是需要搜索的路径
# Target_str是定位的关键字符串
def read_filepath(Path,Target_str):
    Level_1_path = Path
    Level_2_paths = []
    for root,dirs,files in os.walk(Level_1_path):
        for dir in dirs:
            Level_2_path = os.path.join(root,dir)
            Level_2_paths.append(Level_2_path)

    Output_paths = []
    for Level_2_path in Level_2_paths:
        for root,dirs,files in os.walk(Level_2_path):
            for file in files:
                if(Target_str in file):
                    file_path = os.path.join(root,file)
                    Output_paths.append(file_path)

    return Output_paths
# Ouput_paths 由所有满足Target_str的文件路径组成