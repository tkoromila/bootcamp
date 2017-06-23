import numpy as np
import scipy.stats

import seaborn as sns

import Practice_3_ECDF

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

x_rnd = np.random.random(size-100000)

#Make ECDF
x, y = Practice_3_ECDF.ecdf(x_rnd)

# Plot CDF from random numbers (for plotting purposes, only plot 100 points)
fig, ax = plt.subplots(1, 1)
_ = ax.plot(x[::1000], y[::1000], marker='.', linestyle='none', markersize=10)\
                color+'dodgerblue'
# Plot expected CDF (just a straight line from (0,0) to (1,1)
_ = ax.plot([0, 1], [0, 1], color='tomato')

plt.show()
