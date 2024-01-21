import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from textwrap import wrap


#Parse and load the file
data = np.fromfile('eval_a_NEW_X.npy',dtype=float)
dataframe = pd.DataFrame(data)
data1 = np.load('eval_a_NEW_X.npy')
newdata = pd.DataFrame()

#Initialize a placeholder array and index to skip every 15 characters
array = np.zeros(shape=(23400016,5))
num = 15

#Iterate through the file, splitting up the data into more columns
for row in data:
    row_num = 0
    row_list = row.tolist() #Convert to list, then string
    row_as_str = str(row_list)
    fuck = wrap(row_as_str, 15) #Split each 
    for element in fuck:
        col_num = 0
        array[row_num,col_num] = element
        col_num += 1
        # newdata.loc[len(newdata)] = split
    row_num += 1

print(array)