import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

# set up defaults
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# Load in data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

#Set up nice bin widths
bins = np.arange(1700, 2501, 50)

#set up plot
fig, ax = plt.subplots(1, )
_ = ax.set_xlabel('Cross-sectional area (µm$^2$)')
_ = ax.set_ylabel('count')


#Paint the data
_ = ax.hist(xa_low, bins=bins)

#save
fig.savefig('practice_histogram.pdf')

plt.show()
