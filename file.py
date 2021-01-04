from os import getcwd
from os import walk
from os import path
import pandas as pd
current_path = getcwd()
Targetstr1 = 'xls'
Targetstr2 = 'xlsx'

filepaths = []
for root,dirs,files in walk(current_path):
    for file in files:
        if(Targetstr1 in file):
            filepaths.append(path.join(root,file))
        elif(Targetstr2 in file):
            filepaths.append(path.join(root,file))

data = pd.DataFrame()
for i in range(0,len(filepaths)):
    data_1 = pd.read_excel(filepaths[i])
    data = data.append(data_1)
    print(filepaths[i])
print(f'共计合并{len(filepaths)}个文件')

data.to_excel(current_path+'\\output.xls',index=0)