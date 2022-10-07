from plot_data import radial_profile


def absorbance(a, n, conc, e):
    s = 0
    for i in range(0, n):
        s = s + conc[i]
    return e*s*(a/n)


time = 3600  # time in seconds
a = 10  # radius in cm
D = 1e-6  # Diffusion coefficient in cm2/s
conc = 100  # Concentration in ppm
n_point_r = 100  # Number of subdivisions of the radius
e = 910  # extinction coefficient in

y_r = radial_profile(time, a, D, conc, n_point_r)
print(absorbance(a, n_point_r, y_r[0], e))