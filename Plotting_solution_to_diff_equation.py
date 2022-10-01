# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:18:02 2022

@author: Arpit.Shrivastava
"""

import matplotlib.pyplot as plt
from dehyroxy_func import C
a = 0.05
for t in range(0, 3600, 300):
    t_plot = []
    for i in range(0, 250):
        t_plot.append(C((i/250)*a, t, a))
        print(t, " step's", i, " iteration done.")
    plt.plot(t_plot, label=str(t))
    print(t, " step done.")

plt.show()




