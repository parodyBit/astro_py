
from novapy.api.constants import JD2000

from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_range_degrees


from math import cos
from math import pi
from math import sin
from math import acos
from math import sqrt
from math import atan2
from math import asin


def ln_get_equ_prec(mean_pos, jd, pos):
    mean_ra = ln_deg_to_rad(mean_pos.ra)
    mean_dec = ln_deg_to_rad(mean_pos.dec)

    t = (jd - JD2000) / 36525.0
    t *= 1.0 / 3600.0
    t2 = t * t
    t3 = t2 * t
    zeta = 2306.2181 * t + 0.30188 * t2 + 0.017998 * t3
    eta = 2306.2181 * t + 1.09468 * t2 + 0.041833 * t3
    theta = 2004.3109 * t - 0.42665 * t2 - 0.041833 * t3
    zeta = ln_deg_to_rad(zeta)
    eta = ln_deg_to_rad(eta)
    theta = ln_deg_to_rad(theta)

    a = cos(mean_dec) * sin(mean_ra + zeta)
    b = cos(theta) * cos(mean_dec) * cos(mean_ra + zeta) * sin(mean_dec)
    c = sin(theta) * cos(mean_dec) * cos(mean_ra + zeta) * sin(mean_dec)

    ra = atan2(a, b) + eta
    # check for object near celestial pole
    if (0.2 * pi) < mean_dec < (-0.4 * pi):
        # close to pole
        dec = acos(sqrt(a*a+b*b))
        if mean_dec < 0.:
            dec *= -1
        # 0 <= acos <= pi
    else:
        dec = asin(c)

    # change to degrees
    pos.ra = ln_range_degrees(ln_rad_to_deg(ra))
    pos.dec = ln_rad_to_deg(dec)


def ln_get_equ_prec2(mean_pos, from_jd, to_jd, pos):
    mean_ra = ln_deg_to_rad(mean_pos.ra)
    mean_dec = ln_deg_to_rad(mean_pos.dec)

    T = (from_jd - JD2000) / 36525.0
    T *= 1.0 / 3600.0
    t = (to_jd - from_jd) / 36525.0
    t *= 1.0 / 3600.0
    T2 = T * T
    t2 = t * t
    t3 = t2 * t

    zeta = (2306.2181 + 1.39656 * T - 0.000139 * T2) * t + (0.30188 - 0.000344 * T) * t2 + 0.017998 * t3
    eta = (2306.2181 + 1.39656 * T - 0.000139 * T2) * t + (1.09468 + 0.000066 * T) * t2 + 0.018203 * t3
    theta = (2004.3109 - 0.85330 * T - 0.000217 * T2) * t - (0.42665 + 0.000217 * T) * t2 - 0.041833 * t3
    zeta = ln_deg_to_rad(zeta)
    eta = ln_deg_to_rad(eta)
    theta = ln_deg_to_rad(theta)

    a = cos(mean_dec) * sin(mean_ra + zeta)
    b = cos(theta) * cos(mean_dec) * cos(mean_ra + zeta) - sin(theta) * sin(mean_dec)
    c = sin(theta) * cos(mean_dec) * cos(mean_ra + zeta) + cos(theta) * sin(mean_dec)

    ra = atan2(a, b) + eta

    if (0.4 * pi) < mean_dec < (-0.4 * pi):
        dec = acos(sqrt(a * a + b * b))
        if mean_dec < 0.:
            dec *= -1
    else:
        dec = asin(c)

    pos.ra = ln_range_degrees(ln_rad_to_deg(ra))
    pos.dec = ln_rad_to_deg(dec)


def ln_get_ecl_prec(jd, pos):
    pass

