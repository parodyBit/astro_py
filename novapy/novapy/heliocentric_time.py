from novapy.nutation import ln_get_nutation
from novapy.api.ln_nutation import LnNutation
from novapy.api.ln_helio_posn import LnHelioPosn
from novapy.solar_system.earth import ln_get_earth_helio_coords

from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_range_degrees

from math import sin
from math import cos


def ln_get_heliocentric_time_diff(jd, equ_obj):
    earth = LnHelioPosn()
    nutation = LnNutation()

    ln_get_nutation(jd, nutation)
    ln_get_earth_helio_coords(jd, earth)

    theta = ln_deg_to_rad(ln_range_degrees(earth.l + 180))
    ra = ln_deg_to_rad(equ_obj.ra)
    dec = ln_deg_to_rad(equ_obj.dec)
    c_dec = cos(dec)
    obliq = ln_deg_to_rad(nutation.ecliptic)

    return -0.0057755 * earth.r * (cos(theta) * cos(ra) * c_dec + sin(theta)) * \
        (sin(obliq) * sin(dec) + cos(obliq) * c_dec * sin(ra))





