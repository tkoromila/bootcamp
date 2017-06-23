import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import pandas as pd

import Practice_3_ECDF

# Plotting modules and settings.

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')


ax = sns.swarmplot(data=df, x='ID', y='impact force (mN)', hue='date')
ax.set_ylabel('impact force (mN)')
ax.set_xlabel('')

# Remove the legend, it is too large and cumbersome
ax.legend_.remove()

plt.show()
