from math import cos
from math import sin
from math import tan
from novapy.api.ln_helio_posn import LnHelioPosn
from novapy.utility import ln_deg_to_rad



class LnVsop:
    A = float
    B = float
    C = float

    def __init__(self, a, b, c):
        self.A = a
        self.B = b
        self.C = c


def ln_calc_series(data, t):
    value = 0.0
    i = int

    for datum in data:
        value += datum.A * cos(datum.B + datum.C * t)
    return value

#  Transform from VSOP87 to FK5 reference frame


def ln_vsop_to_fk5(position, jd):

    #  get julian centuries from 2000
    T = (jd - 2451545.0) / 36525.0
    LL = position.l + (-1.397 - 0.00031 * T) * T
    LL = ln_deg_to_rad(LL)
    cos_LL = cos(LL)
    sin_LL = sin(LL)
    B = ln_deg_to_rad(position.b)

    delta_L = (-0.09033 / 3600.0) + (0.03916 / 3600.0) * (cos_LL + sin_LL) * tan(B)
    delta_B = (0.03916 / 3600.0) * (cos_LL - sin_LL)

    position.l += delta_L
    position.b += delta_B


