import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

# set up defaults
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

x = np.linspace(-2*np.pi, 2*np.pi, 50)
y = np.sin(x)

fig, ax = plt.subplots(1, )

_ = ax.set_xlabel('x')
_ = ax.set_ylabel('sin(x)')
_ = ax.set_xticks(np.pi*np.array([-2, -1, 0, 1, 2]))
_ = ax.set_xticks(['-2π', '-π', '0', 'π', '2π'])



#Paint
_ = ax.plot(x, y)

plt.show()
