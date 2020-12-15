import pandas as pd

def data_ope(filepath):
    data = pd.read_csv(filepath)
    parameter = 11
    a = data.loc[data['10']==parameter]
    Del_columns = data.columns[2:10]
    a.drop(Del_columns,axis=1,inplace=True)
    a.drop('Record',axis=1,inplace=True)
    a = a.iloc[:,0:48]

    def ouput_mean_tocsv(a,Start_point):
        i = 0
        Output = a.iloc[0:0,:]
        point = 0
        while i < len(a['Date/Time']):
            if( Start_point in str(a['Date/Time'][i:i+1].values)):
                point = i
                break
            i = i +1
        if(point == 0):
            return
        while((i-point)<60):
            Output = Output.append(a.iloc[i:i+1,:],ignore_index=True)
            i = i + 1

        Mean = Output.mean()
        Output = Output.append(Mean,ignore_index=True)
        Output.loc[60,'Date/Time'] = 'Mean' + filepath[69:80] + 'T' + str(Start_point[0:2] + Start_point[3:5])
        Outpath = filepath[0:75] + 'Time' + '.csv'
        # + str(Start_point[0:2] + Start_point[3:5]) 
        Output.to_csv(Outpath,index=0)

    Search_points = ['07:30','19:30']
    for Search_point in Search_points:
        ouput_mean_tocsv(a,Search_point)