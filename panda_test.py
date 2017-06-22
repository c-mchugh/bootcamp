import numpy as np

# Pandas, conventionally imported as pd
import pandas as pd

# Plotting modules and settings.
import matplotlib.pyplot as plt
import seaborn as sns

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

# Read in data files with pandas
df_high = pd.read_csv('data/xa_high_food.csv', comment='#', header=None)
df_low = pd.read_csv('data/xa_low_food.csv', comment='#', header=None)

# rename columns

df_low.columns = ['low']
df_high.columns = ['high']

# concat

df = pd.concat((df_low, df_high), axis=1)

# tidy the data

df = pd.melt(df, var_name="food density", value_name="cross-sectional area (sq µm)")

# write out csv

df.to_csv('xa_combined.csv', index=False)
