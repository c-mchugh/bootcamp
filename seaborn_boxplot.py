import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set up default style of plots

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style="whitegrid", palette=colors, rc={'axes.labelsize': 16})

# import frog data
df = pd.read_csv("data/frog_tongue_adhesion.csv", comment="#")

ax = sns.boxplot(data=df, x="ID", y="impact force (mN)")
ax.set_ylabel("impact force (mN)")
ax.set_xlabel("")


plt.show()
