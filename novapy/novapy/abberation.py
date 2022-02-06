from math import sqrt
from math import asin
from math import atan
from math import atan2
from math import acos
from math import cos
from math import sin
from math import tan
from math import pi

from novapy.api.ln_helio_posn import LnHelioPosn
from novapy.utility import ln_range_degrees
from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg


from novapy.solar_system.solar import ln_get_solar_equ_coords
from novapy.solar_system.solar import ln_get_solar_geom_coords




class Arg:
    def __init__(self, a_l2,a_l3,a_l4,a_l5,a_l6, a_l7, a_l8, a_ll, a_d, a_mm, a_f):
        self.a_L2 = a_l2
        self.a_L3 = a_l3
        self.a_L4 = a_l4
        self.a_L5 = a_l5
        self.a_L6 = a_l6
        self.a_L7 = a_l7
        self.a_L8 = a_l8
        self.a_LL = a_ll
        self.a_D = a_d
        self.a_MM = a_mm
        self.a_F = a_f

class XYZ:
    def __init__(self, sin1, sin2, cos1, cos2):
        self.sin1 = sin1
        self.sin2 = sin2
        self.cos1 = cos1
        self.cos2 = cos2

arguments = [
    Arg(0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    Arg(0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    Arg(0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0),
    Arg(0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 2, 0, -1, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 3, -8, 3, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 5, -8, 3, 0, 0, 0, 0, 0, 0, 0),
    Arg(2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    Arg(0, 1, 0, -2, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
    Arg(0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    Arg(2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 1, 0, -1, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 3, 0, -2, 0, 0, 0, 0, 0, 0, 0),
    Arg(1, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(2, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0),
    Arg(2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 3, -2, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 0, 0, 0, 0, 0, 1, 2, -1, 0),
    Arg(8, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(8, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 2, 0, -2, 0, 0, 0, 0, 0, 0, 0),
    Arg(3, -3, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 2, -2, 0, 0, 0, 0, 0, 0, 0, 0),
    Arg(0, 0, 0, 0, 0, 0, 0, 1, -2, 0, 0)]

x_coefficients = [
    XYZ(-1719914, -2, -25, 0), XYZ(6434, 141, 28007, -107), XYZ(715, 0, 0, 0),
    XYZ(715, 0, 0, 0), XYZ(486, -5, -236, -4), XYZ(159, 0, 0, 0), 
    XYZ(0, 0, 0, 0), XYZ(39, 0, 0, 0), XYZ(33, 0, -10, 0), 
    XYZ(31, 0, 1, 0), XYZ(8, 0, -28, 0), XYZ(8, 0, -28, 0),
    XYZ(21, 0, 0, 0), XYZ(-19, 0, 0, 0), XYZ(17, 0, 0, 0),
    XYZ(16, 0, 0, 0), XYZ(16, 0, 0, 0), XYZ(11, 0, -1, 0),
    XYZ(0, 0, -11, 0), XYZ(-11, 0, -2, 0), XYZ(-7, 0, -8, 0),
    XYZ(-10, 0, 0, 0), XYZ(-9, 0, 0, 0), XYZ(-9, 0, 0, 0),
    XYZ(0, 0, -9, 0), XYZ(0, 0, -9, 0), XYZ(8, 0, 0, 0),
    XYZ(8, 0, 0, 0), XYZ(-4, 0, -7, 0), XYZ(-4, 0, -7, 0),
    XYZ(-6, 0, -5, 0), XYZ(-1, 0, -1, 0), XYZ(4, 0, -6, 0),
    XYZ(0, 0, -7, 0), XYZ(5, 0, -5, 0), XYZ(5, 0, 0, 0)]

y_coefficients = [
    XYZ(25, -13, 1578089, 156), XYZ(25697, -95, -5904, -130), XYZ(6, 0, -657, 0),
    XYZ(0, 0, -656, 0), XYZ(-216, -4, -446, 5), XYZ(2, 0, -147, 0),
    XYZ(0, 0, 26, 0), XYZ(0, 0, -36, 0), XYZ(-9, 0, -30, 0),
    XYZ(1, 0, -28, 0), XYZ(25, 0, 8, 0), XYZ(-25, 0, -8, 0),
    XYZ(0, 0, -19, 0), XYZ(0, 0, 17, 0), XYZ(0, 0, -16, 0),
    XYZ(0, 0, 15, 0), XYZ(1, 0, -15, 0), XYZ(-1, 0, -10, 0),
    XYZ(-10, 0, 0, 0), XYZ(-2, 0, 9, 0), XYZ(-8, 0, 6, 0),
    XYZ(0, 0, 9, 0), XYZ(0, 0, -9, 0), XYZ(0, 0, -8, 0),
    XYZ(-8, 0, 0, 0), XYZ(8, 0, 0, 0), XYZ(0, 0, -8, 0),
    XYZ(0, 0, -7, 0), XYZ(-6, 0, -4, 0), XYZ(6, 0, -4, 0),
    XYZ(-4, 0, 5, 0), XYZ(-2, 0, -7, 0), XYZ(-5, 0, -4, 0),
    XYZ(-6, 0, 0, 0), XYZ(-4, 0, -5, 0), XYZ(0, 0, -5, 0)]

z_coefficients = [
    XYZ(10, 32, 684185, -358), XYZ(11141, -48, -2559, -55), XYZ(-15, 0, -282, 0),
    XYZ(0, 0, -285, 0), XYZ(-94, 0, -193, 0), XYZ(-6, 0, -61, 0),
    XYZ(0, 0, 59, 0), XYZ(0, 0, 16, 0), XYZ(-5, 0, -13, 0),
    XYZ(0, 0, -12, 0), XYZ(11, 0, 3, 0), XYZ(-11, 0, -3, 0),
    XYZ(0, 0, -8, 0), XYZ(0, 0, 8, 0), XYZ(0, 0, -7, 0),
    XYZ(1, 0, 7, 0), XYZ(-3, 0, -6, 0), XYZ(-1, 0, 5, 0),
    XYZ(-4, 0, 0, 0), XYZ(-1, 0, 4, 0), XYZ(-3, 0, 3, 0),
    XYZ(0, 0, 4, 0), XYZ(0, 0, -4, 0), XYZ(0, 0, -4, 0),
    XYZ(-3, 0, 0, 0), XYZ(3, 0, 0, 0), XYZ(0, 0, -3, 0),
    XYZ(0, 0, -3, 0), XYZ(-3, 0, 2, 0), XYZ(3, 0, -2, 0),
    XYZ(-2, 0, 2, 0), XYZ(1, 0, -4, 0), XYZ(-2, 0, -2, 0),
    XYZ(-3, 0, 0, 0), XYZ(-2, 0, -2, 0), XYZ(0, 0, -2, 0)]


def ln_get_equ_aber(mean_pos, jd, equ_pos):
    # speed of light in 10-8 au per day
    c = 17314463350.0

    # calc T
    T = (jd - 2451545.0) / 36525.0


    # calc planetary perturbutions
    L2 = 3.1761467 + 1021.3285546 * T
    L3 = 1.7534703 + 628.3075849 * T
    L4 = 6.2034809 + 334.0612431 * T
    L5 = 0.5995464 + 52.9690965 * T
    L6 = 0.8740168 + 21.329909095 * T
    L7 = 5.4812939 + 7.4781599 * T
    L8 = 5.3118863 + 3.8133036 * T
    LL = 3.8103444 + 8399.6847337 * T
    D = 5.1984667 + 7771.3771486 * T
    MM = 2.3555559 + 8328.6914289 * T
    F = 1.6279052 + 8433.4661601 * T

    X = 0
    Y = 0
    Z = 0

    for idx, arg in enumerate(arguments):
        A = arg.a_L2 * L2 + arg.a_L3 * L3 + \
            arg.a_L4 * L4 + arg.a_L5 * L5 + \
            arg.a_L6 * L6 + arg.a_L7 * L7 + \
            arg.a_L8 * L8 + arg.a_LL * LL + \
            arg.a_D * D + arg.a_MM * MM + \
            arg.a_F * F

        X += (x_coefficients[idx].sin1 + x_coefficients[idx].sin2 * T) * sin(A) + \
            (x_coefficients[idx].cos1 + x_coefficients[idx].cos2 * T) * cos(A)
        Y += (y_coefficients[idx].sin1 + y_coefficients[idx].sin2 * T) * sin(A) + \
            (y_coefficients[idx].cos1 + y_coefficients[idx].cos2 * T) * cos(A)
        Z += (z_coefficients[idx].sin1 + z_coefficients[idx].sin2 * T) * sin(A) + \
            (z_coefficients[idx].cos1 + z_coefficients[idx].cos2 * T) * cos(A)

    #
    mean_ra = ln_deg_to_rad(mean_pos.ra)
    mean_dec = ln_deg_to_rad(mean_pos.dec)

    delta_ra = (Y * cos(mean_ra) - X * sin(mean_ra)) / (c * cos(mean_dec))
    delta_dec = (X * cos(mean_ra) + Y * sin(mean_ra)) * sin(mean_dec) - Z * cos(mean_dec)
    delta_dec /= -c

    equ_pos.ra = ln_rad_to_deg(mean_ra + delta_ra)
    equ_pos.dec = ln_rad_to_deg(mean_dec + delta_dec)



def ln_get_ecl_aber(mean_pos, jd, lnlat_pos):
    sol_posn = LnHelioPosn()
    k = ln_deg_to_rad(20.49552 * (1.0 / 3600.0))

    T = (jd - 2451545) / 36525
    T2 = T * T

    ln_get_solar_geom_coords(jd, sol_posn)
    true_longitude = ln_deg_to_rad(sol_posn.b)

    e = 0.016708617 - 0.000042037 * T - 0.0000001236 * T2
    e = ln_deg_to_rad(e)

    t = 102.93735 + 1.71953 * T + 0.000046 * T2
    t = ln_deg_to_rad(t)

    mean_lng = ln_deg_to_rad(mean_pos.lng)
    mean_lat = ln_deg_to_rad(mean_pos.lat)

    delta_lng = (-k * cos(true_longitude - mean_lng) + e * k * cos(t - mean_lng)) / cos(mean_lat)

    delta_lat = (-1 * k) * sin(mean_lat)*(sin(true_longitude - mean_lng) - e * sin(t - mean_lng))

    mean_lng += delta_lng
    mean_lat += delta_lat

    lnlat_pos.lng = ln_rad_to_deg(mean_lng)
    lnlat_pos.lat = ln_rad_to_deg(mean_lat)
