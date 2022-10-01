# This script implements the solution to diffusion equation
# in an infinitely long cylinder. The solution is taken from
# Mathematics of diffusion by Crank.

import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc
import scipy.integrate as integrate
from math import exp

n = 500  # number of terms for the series
r = 0.8  # distance from center at which concentration needed
t = 1000  # time at which concentration is needed
D = 10e-6  # Diffusion coefficient
a = 1  # radius of cylinder


def f(x):  # Initial distribution of OH in preform
    return 5


# Calculation of n roots
alpha = sc.jn_zeros(0, n)

series_sum = 0  # To store sum of series terms
series_sum_array = []

for i in range(0, n):
    al = alpha[i]
    exp_term = exp(-D*al*al*t)
    bessel_term = (sc.j0(r*al))/(np.square(sc.j1(a*al)))
    integral_term = integrate.quad(lambda x: x*f(x)*sc.j0(x*al), 0, a, limit=1000)
    series_sum_array.append(series_sum)
    series_sum = series_sum + exp_term * bessel_term * integral_term[0]
    print((i/n)*100 , "% done.")
    # series_sum = series_sum + exp_term * bessel_term * 1
    # print(series_sum, exp_term, bessel_term)

C = (2/(a*a))*series_sum
plt.plot(series_sum_array)
plt.show()
print(C)

