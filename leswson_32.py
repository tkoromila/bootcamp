import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


import Practice_3_ECDF

# Plotting modules and settings.

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')
df.loc[np.abs(df['adhesive strength (Pa)'])<2000, 'impact time (ms)']

#plt.show()
