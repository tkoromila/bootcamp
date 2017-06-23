import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

# set up defaults
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

#load data
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')

#slice
t = data[:, 0]
V = data[:, 1]

#Build
fig, ax = plt.subplots(1, 1, figsize=(10, 3))
_ = ax.set_xlabel('t (ms)')
_ = ax.set_ylabel('V (μV)')
#ax.set_xlim(1200, 1500)

#Paint
_ = ax.plot(t, V)

plt.show()
