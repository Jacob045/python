
import numpy as np
import pandas as pd

MSE_data = pd.DataFrame()

print(MSE_data)

row = 0
while row < 3:
    MSE_data.loc[0,row] = row
    MSE_data.loc[1,row] = row +10
    row = row + 1

print(MSE_data)