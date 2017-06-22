import numpy as np
import matplotlib.pyplot as plt

def ecdf(data):
    """Compute x, y values for an empirical distribution function."""
    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)
    return x, y

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

fig, ax = plt.subplots(1,1)

_ = ax.set_xlabel('beak depth (mm)')
_ = ax.set_ylabel('ECDF')
_ = ax.plot (x_1975, y_1975, marker='.', linestyle='none', label='1975')
_ = ax.plot (x_2012, y_2012, marker='.', linestyle='none', label='2012')

ax.legend(loc='lower right')

plt.show()
