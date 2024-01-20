import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
data = np.load('p00_n1_X.npy')
for i in range(len(data)):
    plt.img(data[i], cmap='gray')
    plt.show()