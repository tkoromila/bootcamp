# import numpy as np
#
# # Pandas, conventionally imported as pd
import pandas as pd
#
# # Plotting modules and settings.
# import matplotlib.pyplot as plt
# import seaborn as sns
# colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
#           '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
#           '#bcbd22', '#17becf']
# sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})
#
# # The following is specific Jupyter notebooks
# %matplotlib inline
# %config InlineBackend.figure_formats = {'png', 'retina'}

#dictionary
wc_dict = { 'Klose':16,
            'Ronaldo': 15,
            'Muller': 14,
            'Fontaine': 13,
            'Pele': 12,
            'Kocsis':11,
            'Klinsmann': 11,}

#dictionary
nation_dict = {'Klose': 'Germany',
               'Ronaldo': 'Brazil',
               'Muller': 'Germany',
               'Fontaine': 'France',
               'Pele': 'Brazil',
               'Kocsis': 'Hungary',
               'Klinsmann': 'Germany,}


# Series with nations
s_nation = pd.Series(nation_dict)

# convert dictionary
s_goals = pd.Series(wc_dict)

# Look at it
s_nation

# Combine into a DataFrame
df_wc = pd.DataFrame({'nation': s_nation, 'goals': s_goals})

# Take a look
df_wc


# #print both
# print(s_goals)
# print(s_nation)
