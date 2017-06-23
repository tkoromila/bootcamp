import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')
df

# Slice out big forces
df_big_force = df.loc[df['impact force (mN)'] > 1000, :]

# Look at it
df_big_force

fig, ax = plt.subplots(1, 1)
ax.set_xlabel('impact force')
ax.set_ylabel('adhesive force')
_ = ax.plot(df['impact force (mN)'], df['adhesive force (mN)'], marker='.', linestyle='none')

df.plot(x='total contact area (mm2)', y='adhesive force (mN)', kind='scatter')

plt.show()

df = df.rename(columns={'impact force (mN)': 'impf'})
