import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/frog_tongue_adhesion.csv', comment='#')

#group by ind frogs
grouped = df.groupy('ID')
