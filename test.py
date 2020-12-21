from datetime import date
from os.path import join
from numpy.lib.function_base import append
from numpy.lib.utils import info
import pandas as pd
import numpy as np
import os

from pandas.io.parsers import read_csv
filepath = r'H:\桌面\榜样的力量参会人员名单\demo'
Target_str = 'xlsx'

Output = pd.DataFrame()
i = 1
for root,dirs,files in os.walk(filepath):
    for file in files:
        print(i)
        i = i+ 1
        if(Target_str in file):
            # print(filepath +'\\' + file)
            data =pd.read_excel(filepath +'\\' + file)
            print(data.info())
            Output = Output.append(date)
            # Output_paths.append(os.path,join((root,file)))

