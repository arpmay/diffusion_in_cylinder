# THIS IS THE NUMERICAL CALCULATION FOR THE ANALYTICAL SOLUTION
# OF FICK'S EQUATION FOR A CYLINDER. REFER 'MATHEMATICS OF DIFFUSION'
# BY CRANK FOR THE THEORY.


import scipy.special as sc
import scipy.integrate as integrate
from math import exp


def C(r, t, a, conc, D, n=100):
    a_alpha = sc.jn_zeros(0, n)
    series_sum = 0
    for i in range(0, n):
        al = a_alpha[i]/a
        exp_term = exp(-D * al * al * t)
        bessel_term = (sc.j0(r * al)) / ((sc.j1(a * al))*(sc.j1(a * al)))
        integral_term = integrate.quad(lambda x: x * conc * sc.j0(x * al), 0, a, limit=250)
        series_sum = series_sum + exp_term * bessel_term * integral_term[0]

    c = (2 / (a * a)) * series_sum
    return c
