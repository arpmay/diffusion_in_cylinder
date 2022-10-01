# THIS FUNCTION DOES TWO THINGS:
# 1. CALCULATE CONC. FOR ONE POINT ON DIFFERENT TIMES-> TEMPORAL PROFILE
# 2. CALCULATE CONC. FOR ONE INSTANT FOR DIFFERENT POINTS-> RADIAL PROFILE
import matplotlib.pyplot as plt

from dehyroxy_func import C


def radial_profile(t, a, D, conc, n=250):
    r_plot = []
    for i in range(0, n):
        r_plot.append(C((i / n) * a, t, a, conc, D))
    return r_plot


def temporal_profile(r, a, T, dT, D, conc, n=250):
    t_plot = []
    for i in range(0, T, dT):
        t_plot.append(C(r, i, a, conc, D))
    return t_plot

