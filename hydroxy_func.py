import scipy.special as sc
from math import exp


def C(C0, r, t, a=1, D=1e-5, n=100):
    alpha = sc.jn_zeros(0, n)
    series_sum = 0
    for i in range(0, n):
        al = alpha[i]/a
        exp_term = exp(-D * al * al * t)
        bessel_term = (sc.j0(r * al)) / (sc.j1(a * al))
        series_sum = series_sum + exp_term * bessel_term * (1/al)
        # print(int((i / n)*100), "% done.")

    c = 1 - (2/a)*series_sum
    return c*C0

