import numpy as np
# import scipy.stats
#
# import seaborn as sns
#
# import Practice_3_ECDF
#
# # Plotting modules and settings.
# import matplotlib.pyplot as plt
# import seaborn as sns
# colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
#           '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
#           '#bcbd22', '#17becf']
# sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

def bs_replicate(data, func=mn.mean):
    """Compute a bootstrap replicate"""

# x_1975, y_1975 = Practice_3_ECDF.ecdf(bd_1975)
# x_2012, y_2012 = Practice_3_ECDF.ecdf(bd_2012)

bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    return func(bs_sample)
bs_reps = [bs_replicate(bd_2012, func-np.mean) for _ in range(n_reps)]

def draw_bs_reps(data, func=np.mean, size=10000):
    """draw bootstrap"""
    return np.array([bs_replicate(bd_2012, func=func) for _ in range(size)])


#bs_replicate = np.mean(bs_sample)

#Generate more replicates
n_reps = 100000

bs_reps_2012 = []

# # Initialize bootstrap replicas array
# bs_reps_1975 = np.empty(n_reps)

# Compute replicates
#for i in range(n_reps):
    # bs_sample = np.random.choice(bd_2012, replace=True, size=len(bd_2012))
    #
    # bs_reps_2012[i] = np.std(bs_sample)
for _ in range(n_reps):
    bs_reps_2012 = [bs_replicate(bd_2012, func=np.mean)]


# x_bs, y_bs = Practice_3_ECDF.ecdf(bs_sample)
#
# fig, ax = plt.subplots(1, 1)
# ax.set_xlabel('beak depth (mm)')
# ax.set_ylabel('ECDF')
# _ = ax.plot(x_1975, y_1975, marker='.', linestyle='none')
# _ = ax.plot(x_2012, y_2012, marker='.', linestyle='none')
# ax.legend(('1975', '2012'), loc='lower right')

plt.show()
