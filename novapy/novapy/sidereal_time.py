from novapy.utility import ln_range_degrees
from novapy.utility import ln_deg_to_rad
from novapy.nutation import ln_get_nutation
from novapy.api.ln_nutation import LnNutation

from math import cos


def ln_get_mean_sidereal_time(jd):
    t = (jd - 2451545.0) / 36525.0
    # calc mean angle
    sidereal = 280.46061837 + (360.98564736629 * (jd - 2451545.0))
    + (0.000387933 * t * t) - (t * t * t / 38710000.0)
    # add a convenient multiple of 360 degrees
    sidereal = ln_range_degrees(sidereal)
    # change to hours
    sidereal *= 24 / 360
    return sidereal


def ln_get_apparent_sidereal_time(jd):
    n = LnNutation
    sidereal = ln_get_mean_sidereal_time(jd)
    # add corrections for nutation in longitude and for the true obliquity
    # of the ecliptic

    ln_get_nutation(jd, n)
    correction = (n.longitude / 15.0 * cos(ln_deg_to_rad(n.obliquity)))
    sidereal += correction
    return sidereal
