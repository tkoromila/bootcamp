import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

# set up defaults
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#ecdf(data)
def ecdf(data):

    x = np.sort(data)
    y = np.arange(1, len(data)+1)/len(data)
    return x, y

# Load in data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')


#Build
fig, ax = plt.subplots(1, 1)
_ = ax.set_xlabel('Cross-sectional area')
_ = ax.set_ylabel('ECDF')

#Compute ECDF for plotting
x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)


#Paint
_ = ax.plot(x_high, y_high, marker='o', linestyle='none')
_ = ax.plot(x_low, y_low, '.', linestyle='none')


plt.show()
