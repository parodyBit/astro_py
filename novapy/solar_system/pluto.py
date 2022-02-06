from math import sqrt
from math import asin
from math import atan2
from math import acos
from math import log10
from math import sin
from math import cos

from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_range_degrees

from novapy.vsop87 import LnVsop
from novapy.vsop87 import ln_calc_series
from novapy.vsop87 import ln_vsop_to_fk5

from novapy.solar_system.earth import ln_get_earth_helio_coords
from novapy.solar_system.earth import ln_get_earth_solar_dist
from novapy.solar_system.solar import ln_get_solar_geom_coords

from novapy.api.ln_helio_posn import LnHelioPosn
from novapy.api.ln_rect_posn import LnRectPosn
from novapy.riseset import ln_get_body_rst_horizon
from novapy.transform import ln_get_rect_from_helio
from novapy.api.constants import LN_STAR_STANDARD_HORIZON



class pluto_argument:
    j = 0.0
    s = 0.0
    p = 0.0

    def __init__(self, j, s, p):
        self.j = j
        self.s = s
        self.p = p
class pluto_longitude:
    a = 0.0
    b = 0.0

    def __init__(self, a, b):
        self.a = a
        self.b = b


class pluto_latitude:
    a = 0.0
    b = 0.0

    def __init__(self, a, b):
        self.a = a
        self.b = b


class pluto_radius:
    a = 0.0
    b = 0.0

    def __init__(self, a, b):
        self.a = a
        self.b = b


argument = [
    pluto_argument(0, 0, 1),
    pluto_argument(0, 0, 2), pluto_argument(0, 0, 3),
    pluto_argument(0, 0, 4), pluto_argument(0, 0, 5),
    pluto_argument(0, 0, 6), pluto_argument(0, 1, -1),
    pluto_argument(0, 1, 0), pluto_argument(0, 1, 1),
    pluto_argument(0, 1, 2), pluto_argument(0, 1, 3),
    pluto_argument(0, 2, -2), pluto_argument(0, 2, -1),
    pluto_argument(0, 2, 0), pluto_argument(1, -1, 0),
    pluto_argument(1, -1, 1), pluto_argument(1, 0, -3),
    pluto_argument(1, 0, -2), pluto_argument(1, 0, -1),
    pluto_argument(1, 0, 0), pluto_argument(1, 0, 1),
    pluto_argument(1, 0, 2), pluto_argument(1, 0, 3),
    pluto_argument(1, 0, 4), pluto_argument(1, 1, -3),
    pluto_argument(1, 1, -2), pluto_argument(1, 1, -1),
    pluto_argument(1, 1, 0), pluto_argument(1, 1, 1),
    pluto_argument(1, 1, 3), pluto_argument(2, 0, -6),
    pluto_argument(2, 0, -5), pluto_argument(2, 0, -4),
    pluto_argument(2, 0, -3), pluto_argument(2, 0, -2),
    pluto_argument(2, 0, -1), pluto_argument(2, 0, 0),
    pluto_argument(2, 0, 1), pluto_argument(2, 0, 2),
    pluto_argument(2, 0, 3), pluto_argument(3, 0, -2),
    pluto_argument(3, 0, -1), pluto_argument(3, 0, 0)]

longitude = [
    pluto_longitude(-19799805, 19850055),
    pluto_longitude(897144, -4954829),
    pluto_longitude(611149, 1211027),
    pluto_longitude(-341243, -189585),
    pluto_longitude(129287, -34992),
    pluto_longitude(-38164, 30893),
    pluto_longitude(20442, -9987),
    pluto_longitude(-4063, -5071),
    pluto_longitude(-6016, -3336),
    pluto_longitude(-3956, 3039), pluto_longitude(-667, 3572),
    pluto_longitude(1276, 501), pluto_longitude(1152, -917),
    pluto_longitude(630, -1277), pluto_longitude(2571, -459),
    pluto_longitude(899, -1449), pluto_longitude(-1016, 1043),
    pluto_longitude(-2343, -1012), pluto_longitude(7042, 788),
    pluto_longitude(1199, -338), pluto_longitude(418, -67),
    pluto_longitude(120, -274), pluto_longitude(-60, -159),
    pluto_longitude(-82, -29), pluto_longitude(-36, -20),
    pluto_longitude(-40, 7), pluto_longitude(-14, 22),
    pluto_longitude(4, 13), pluto_longitude(5, 2),
    pluto_longitude(-1, 0), pluto_longitude(2, 0),
    pluto_longitude(-4, 5), pluto_longitude(4, -7),
    pluto_longitude(14, 24), pluto_longitude(-49, -34),
    pluto_longitude(163, -48), pluto_longitude(9, 24),
    pluto_longitude(-4, 1), pluto_longitude(-3, 1),
    pluto_longitude(1, 3), pluto_longitude(-3, -1),
    pluto_longitude(5, -3), pluto_longitude(0, 0)]

latitude = [
    pluto_latitude(-5452852, -14974862),
    pluto_latitude(3527812, 1672790),
    pluto_latitude(-1050748, 327647),
    pluto_latitude(178690, -292153),
    pluto_latitude(18650, 100340),
    pluto_latitude(-30697, -25823),
    pluto_latitude(4878, 11248), pluto_latitude(226, -64),
    pluto_latitude(2030, -836), pluto_latitude(69, -604),
    pluto_latitude(-247, -567), pluto_latitude(-57, 1),
    pluto_latitude(-122, 175), pluto_latitude(-49, -164),
    pluto_latitude(-197, 199), pluto_latitude(-25, 217),
    pluto_latitude(589, -248), pluto_latitude(-269, 711),
    pluto_latitude(185, 193), pluto_latitude(315, 807),
    pluto_latitude(-130, -43), pluto_latitude(5, 3),
    pluto_latitude(2, 17), pluto_latitude(2, 5),
    pluto_latitude(2, 3), pluto_latitude(3, 1),
    pluto_latitude(2, -1), pluto_latitude(1, -1),
    pluto_latitude(0, -1), pluto_latitude(0, 0),
    pluto_latitude(0, -2), pluto_latitude(2, 2),
    pluto_latitude(-7, 0), pluto_latitude(10, -8),
    pluto_latitude(-3, 20), pluto_latitude(6, 5),
    pluto_latitude(14, 17), pluto_latitude(-2, 0),
    pluto_latitude(0, 0), pluto_latitude(0, 0),
    pluto_latitude(0, 1), pluto_latitude(0, 0),
    pluto_latitude(1, 0)]

radius = [
    pluto_radius(66865439, 68951812),
    pluto_radius(-11827535, -332538),
    pluto_radius(1593179, -1438890),
    pluto_radius(-18444, 483220), pluto_radius(-65977, -85431),
    pluto_radius(31174, -6032), pluto_radius(-5794, 22161),
    pluto_radius(4601, 4032), pluto_radius(-1729, 234),
    pluto_radius(-415, 702), pluto_radius(239, 723),
    pluto_radius(67, -67), pluto_radius(1034, -451),
    pluto_radius(-129, 504), pluto_radius(480, -231),
    pluto_radius(2, -441), pluto_radius(-3359, 265),
    pluto_radius(7856, -7832), pluto_radius(36, 45763),
    pluto_radius(8663, 8547), pluto_radius(-809, -769),
    pluto_radius(263, -144), pluto_radius(-126, 32),
    pluto_radius(-35, -16), pluto_radius(-19, -4),
    pluto_radius(-15, 8), pluto_radius(-4, 12),
    pluto_radius(5, 6), pluto_radius(3, 1),
    pluto_radius(6, -2), pluto_radius(2, 2),
    pluto_radius(-2, -2), pluto_radius(14, 13),
    pluto_radius(-63, 13), pluto_radius(136, -236),
    pluto_radius(273, 1065), pluto_radius(251, 149),
    pluto_radius(-25, -9), pluto_radius(9, -2),
    pluto_radius(-8, 7), pluto_radius(2, -10),
    pluto_radius(19, 35), pluto_radius(10, 2)]

def ln_get_pluto_equ_coords(jd, equ_posn):
    h_sol = LnHelioPosn()
    h_pluto = LnHelioPosn()

    g_sol = LnRectPosn()
    g_pluto = LnRectPosn()

    ln_get_solar_geom_coords(jd, h_sol)
    ln_get_rect_from_helio(h_sol, g_sol)
    t = 0
    while True:
        last = t
        ln_get_pluto_helio_coords(jd - t, h_pluto)
        ln_get_rect_from_helio(h_pluto, g_pluto)

        a = g_sol.x + g_pluto.x
        b = g_sol.y + g_pluto.y
        c = g_sol.z + g_pluto.z

        delta = a * a + b * b + c * c
        delta = sqrt(delta)
        t = delta * 0.0057755183
        diff = t - last
        if diff < 0.0001 or diff > -0.0001:
            break

    ra = atan2(b, a)
    dec = c / delta
    dec = asin(dec)

    equ_posn.ra = ln_range_degrees(ln_rad_to_deg(ra))
    equ_posn.dec = ln_rad_to_deg(dec)


def ln_get_pluto_helio_coords(jd, helio_posn):
    t = (jd - 2451545.0) / 36525.0

    j = 34.35 + 3034.9057 * t
    s = 50.08 + 1222.1138 * t
    p = 238.96 + 144.9600 * t
    idx = 0
    sum_longitude = 0
    sum_latitude = 0
    sum_radius = 0
    for i in argument:
        a = i.j * j + i.s * s + i.p * p
        sin_a = sin(ln_deg_to_rad(a))
        cos_a = cos(ln_deg_to_rad(a))
        sum_longitude += longitude[idx].a * sin_a + longitude[idx].b * cos_a
        sum_latitude += latitude[idx].a * sin_a + latitude[idx].b * cos_a
        sum_radius += radius[idx].a * sin_a + radius[idx] * cos_a
        idx += 1

    helio_posn.l = 238.958116 + 144.96 * t + sum_longitude * 0.000001
    helio_posn.b = -3.908239 + sum_latitude * 0.000001
    helio_posn.r = 40.7241346 + sum_radius * 0.0000001





def ln_get_pluto_earth_dist(jd):
    h_pluto = LnHelioPosn()
    h_earth = LnHelioPosn()

    g_pluto = LnRectPosn()
    g_earth = LnRectPosn

    ln_get_pluto_helio_coords(jd, h_pluto)
    ln_get_earth_helio_coords(jd, h_earth)

    ln_get_rect_from_helio(h_pluto, g_pluto)
    ln_get_rect_from_helio(h_earth, g_earth)

    x = g_pluto.x - g_earth.x
    y = g_pluto.y - g_earth.y
    z = g_pluto.z - g_earth.z
    x = x * x
    y = y * y
    z = z * z

    return sqrt(x + y + z)


def ln_get_pluto_solar_dist(jd):
    h_pluto = LnHelioPosn()
    ln_get_pluto_helio_coords(jd, h_pluto)
    return h_pluto.r


def ln_get_pluto_magnitude(jd):
    r = ln_get_pluto_solar_dist(jd)
    delta = ln_get_pluto_earth_dist(jd)
    return -1.0 + 5.0 * log10(r * delta)


def ln_get_pluto_disk(jd):
    R = ln_get_earth_solar_dist(jd)
    r = ln_get_pluto_solar_dist(jd)
    delta = ln_get_pluto_earth_dist(jd)
    return (((r + delta) * (r + delta)) - R * R) / (4.0 * r * delta)


def ln_get_pluto_phase(jd):
    R = ln_get_earth_solar_dist(jd)
    r = ln_get_pluto_solar_dist(jd)
    delta = ln_get_pluto_earth_dist(jd)
    i = (r * r + delta * delta - R * R) / (2.0 * r * delta)
    i = acos(i)
    return ln_rad_to_deg(i)


def ln_get_pluto_rst(jd, obs, rst):
    body_coords = IGetEquBodyCoords()
    body_coords.set_name('pluto')
    return ln_get_body_rst_horizon(jd, obs, body_coords, LN_STAR_STANDARD_HORIZON, rst)



def ln_get_pluto_sdiam(jd):
    # at 1 AU
    So = 2.07
    dist = ln_get_pluto_earth_dist(jd)
    return So / dist


def ln_get_pluto_rect_helio(jd, rect_posn):
    pluto = LnHelioPosn()
    ln_get_pluto_helio_coords(jd, pluto)
    ln_get_rect_from_helio(pluto, rect_posn)


from novapy.util.i_get_equ_body_coords import IGetEquBodyCoords
