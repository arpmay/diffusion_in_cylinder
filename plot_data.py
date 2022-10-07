from dehyroxy_func import C as c_out
from hydroxy_func import C as c_in
from planar_diffusion import planar_diffusion

def radial_profile(t, a, D, conc, n):
    r_plot = []
    plot = []
    for i in range(0, n):
        plot.append(c_out((i / n) * a, t, a, conc, D))
    r_plot.append(plot)
    return r_plot


def temporal_profile(r, a, T, dT, D, conc):
    t_plot = []
    for i in range(0, T, dT):
        t_plot.append(c_out(r, i, a, conc, D))
    return t_plot


def cc_simulation_profile(c_sat=1000, D=8.42e-6, a=16, tin=3600, tout=3600, n_point_r=100, n=100):
    r_plot = []
    for i in range(0, n_point_r):
        r_plot.append(c_out((i / n_point_r) * a, tout, a, c_in(c_sat, (i / n_point_r) * a, tin, a, D, n), D))
    return r_plot


