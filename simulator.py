from hydroxy_func import C as c_in
from dehyroxy_func import C as c_out
from matplotlib import pyplot as plt
# Calculating radial profile after hydroxylation using c_in

c_sat = 1000  # saturation concentration
n = 100  # Number of terms of the series to be summed
D = 8.42e-6  # Diffusion coefficient
a = 16  # Radius of the preform
tin= 3600  # Total time of hydroxylation
tout = 3600 # TOtal time of dehydroxylation
n_point_r = 1000  # No. of divisions to be made in radius/ no. of points at which C will be calculated

r_plot = []
for i in range(0, n_point_r):
    r_plot.append(c_out((i / n_point_r) * a, tout, a, c_in(c_sat, (i / n_point_r) * a, tin, a, D), D))

plt.plot(r_plot)

plt.show()