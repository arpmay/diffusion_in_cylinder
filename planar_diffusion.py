from scipy.special import erf


def planar_diffusion(D, C, r, t):
    return C * (1 - erf(r / (2 * ((D*t) ** 0.5))))
