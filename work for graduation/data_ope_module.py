import pandas as pd

def data_ope(filepath):
    #由文件路径读入数据，初步处理
    data = pd.read_csv(filepath)
    photoname_1 = filepath[69:92]
    parameter = 11
    photoname = photoname_1 + '-' + str(parameter) + '.png'
    a = data.loc[data['10']==parameter]
    Del_columns = data.columns[2:10]
    a.drop(Del_columns,axis=1,inplace=True)
    a.drop('Record',axis=1,inplace=True)
    z = a.iloc[:,1:48].T
    return(z,a,photoname)