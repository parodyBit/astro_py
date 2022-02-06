from novapy.solar_system.earth import ln_get_earth_helio_coords
from novapy.solar_system.earth import ln_get_earth_solar_dist
from novapy.utility import ln_range_degrees

from novapy.transform import ln_get_equ_from_ecl
from novapy.transform import ln_get_rect_from_helio

from novapy.api.ln_helio_posn import LnHelioPosn
from novapy.api.ln_lnlat_posn import LnLnlatPosn


from novapy.riseset import ln_get_body_rst_horizon

from novapy.nutation import ln_get_nutation
from novapy.api.ln_nutation import LnNutation


LN_SOLAR_STANDARD_HORIZON = -0.8333


def ln_get_solar_geom_coords(jd, helio_pos):
    # Calculate geometric coordinates and radius vector accuracy 0.01 arc
    # second error - uses VSOP87 solution.
    #
    # Latitude and Longitude returned are in degrees, whilst radius vector
    # returned is in AU.
    #
    ln_get_earth_helio_coords(jd, helio_pos)
    helio_pos.l += 180.0
    helio_pos.l = ln_range_degrees(helio_pos.l)
    helio_pos.b *= -1.0


def ln_get_solar_equ_coords(jd, equ_pos):
    # Calculate apparent equatorial solar coordinates for given julian day.
    # This function includes the effects of aberration and nutation.
    #

    sol = LnHelioPosn()
    lb = LnLnlatPosn()
    nutation = LnNutation()
    # get geometric coords
    ln_get_solar_geom_coords(jd, sol)
    # get nutation
    ln_get_nutation(jd, nutation)
    sol.l += nutation.longitude
    # aberration
    aberration = (20.4898 / (360.0 * 60.0 * 60.0)) / sol.r
    sol.l -= aberration
    # transform to equatorial
    lb.lat = sol.b
    lb.lng = sol.l
    ln_get_equ_from_ecl(lb, jd, equ_pos)


def ln_get_solar_ecl_coords(jd, lnlat_pos):
    sol = LnHelioPosn()
    nutation = LnNutation()
    # get geometric coords
    ln_get_solar_geom_coords(jd, sol)
    # get nutation
    ln_get_nutation(jd, nutation)
    sol.l += nutation.longitude
    # aberration
    aberration = (20.4898 / (360.0 * 60.0 * 60.0)) / sol.r
    sol.l -= aberration

    lnlat_pos.lng = sol.l
    lnlat_pos.lat = sol.b


def ln_get_solar_geo_coords(jd, rect_pos):
    sol = LnHelioPosn()
    ln_get_earth_helio_coords(jd, sol)

    ln_get_rect_from_helio(sol, rect_pos)
    rect_pos.X *= -1.0
    rect_pos.Y *= -1.0
    rect_pos.Z *= -1.0


def ln_get_solar_rst_horizon(jd, obs, horizon, rst):
    body_coords = IGetEquBodyCoords()
    body_coords.set_name('solar')

    return ln_get_body_rst_horizon(jd, obs, body_coords, horizon, rst)


def ln_get_solar_rst(jd, obs, rst):
    return ln_get_solar_rst_horizon(jd, obs, LN_SOLAR_STANDARD_HORIZON, rst)


def ln_get_solar_sdiam(jd):
    so = 959.63
    dist = ln_get_earth_solar_dist(jd)
    return so / dist
# import down here to prevent circular include
from novapy.util.i_get_equ_body_coords import IGetEquBodyCoords