from hydroxy_func import C as c_in
from dehyroxy_func import C as c_out
# Simulating the entire hydroxylation and dehydroxylation process


def simulation_plot(c_sat=1000, D=8.42e-6, a=16, tin=3600, tout=3600, n_point_r=100, n=100):
    r_plot = []
    for i in range(0, n_point_r):
        r_plot.append(c_out((i / n_point_r) * a, tout, a, c_in(c_sat, (i / n_point_r) * a, tin, a, D, n), D))
    return r_plot

