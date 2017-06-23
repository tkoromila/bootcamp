import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

#group by ind frogs
imp_force_df = df.loc[:, ['ID', 'impact force (mN)']]
grouped = df.groupby('ID')

df_mean = grouped.apply(np.mean)

print(df_mean)
