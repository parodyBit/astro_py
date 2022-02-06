from novapy.api.ln_helio_posn import LnHelioPosn
from novapy.nutation import ln_get_nutation

from novapy.api.ln_nutation import LnNutation
from novapy.sidereal_time import ln_get_mean_sidereal_time
from novapy.sidereal_time import ln_get_apparent_sidereal_time

from decimal import Decimal

from novapy.precession import ln_get_equ_prec2

from novapy.api.constants import JD2000
from novapy.api.constants import B1950
from math import sin
from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_range_degrees

from math import cos
from math import pi
from math import acos
from math import atan2
from math import asin
from math import tan
from math import sqrt


def ln_get_rect_from_helio(obj, pos):
    # Transform an objects heliocentric ecliptical coordinates into
    # heliocentric rectangular coordinates.
    # ecliptic J2000
    sin_e = 0.397777156
    cos_e = 0.917482062

    # calc common values
    cos_b = cos(ln_deg_to_rad(obj.b))
    cos_l = cos(ln_deg_to_rad(obj.l))
    sin_b = sin(ln_deg_to_rad(obj.b))
    sin_l = sin(ln_deg_to_rad(obj.l))

    pos.x = float(obj.r * cos_l * cos_b)
    pos.y = float(obj.r * (sin_l * cos_b * cos_e - sin_b * sin_e))
    pos.z = float(obj.r * (sin_l * cos_b * sin_e + sin_b * cos_e))


def ln_get_hrz_from_equ(obj, obs, jd, pos):
    sidereal = ln_get_mean_sidereal_time(jd)
    ln_get_hrz_from_equ_sidereal_time(obj, obs, sidereal, pos)


def ln_get_hrz_from_equ_sidereal_time(obj, obs, sidereal, pos):
    #change sidereal_time from hours to radians
    sidereal *= 2 * pi / 24
    # calculate hour angle of object at observers position
    ra = ln_deg_to_rad(obj.ra)
    h = sidereal + ln_deg_to_rad(obs.lng) - ra
    # convert to radians - hour angle, observers latitude, object
    # declination
    latitude = ln_deg_to_rad(obs.lat)
    declination = ln_deg_to_rad(obj.dec)
    # misuse of a
    A = sin(latitude) * sin(declination) + cos(latitude) * cos(declination) * h
    # convert back to degrees
    pos.alt = ln_rad_to_deg(h)
    # zenith distance
    # z = acos(A)
    z = cos(A)
    zs = sin(z)

    if abs(zs) < 0.00001:
        if obj.dec > 0.0:
            pos.az = 180.0
        else:
            pos.az = 0.0
        if obj.dec > 0.0 and obs.lat > 0.0 or obj.dec < 0.0 and obs.lat < 0.0:
            pos.alt = 90.0
        else:
            pos.alt = -90.0
        return
    aas = (cos(declination) * sin(h)) / zs
    aac = (sin(latitude) * cos(declination) * cos(h) - cos(latitude * sin(declination))) / zs

    # don't blom at atan2
    if aas == 0.0 and aac == 0.0:
        if obj.dec > 0:
            pos.az = 180
        else:
            pos.az = 0.0
        return
    A = atan2(aas, aac)

    # convert back to degrees
    pos.az = ln_range_degrees(ln_rad_to_deg(A))


def ln_get_equ_from_hrz(obj, obs, jd, pos):
    # Transform an objects horizontal coordinates into equatorial coordinates
    # for the given julian day and observers position.
    a = ln_deg_to_rad(obj.az)
    h = ln_deg_to_rad(obj.alt)

    longitude = ln_deg_to_rad(obs.lng)
    latitude = ln_deg_to_rad(obs.lat)

    h = atan2(sin(a), (cos(a) * sin(latitude) + tan(h) * cos(latitude)))

    declination = sin(latitude) * sin(h) - cos(latitude) * cos(h) * cos(a)
    declination = asin(declination)

    # get ra = sidereal - longitude + H and change sidereal to radians
    sidereal = ln_get_apparent_sidereal_time(jd)
    sidereal *= 2.0 * pi / 24
    pos.ra = ln_range_degrees(ln_rad_to_deg(sidereal - h + longitude))
    pos.dec = ln_rad_to_deg(declination)


def ln_get_equ_from_ecl(obj, jd, pos):
    nutation = LnNutation
    ln_get_nutation(jd, nutation)
    nutation.ecliptic = ln_deg_to_rad(nutation.ecliptic)

    longitude = ln_deg_to_rad(obj.lng)
    latitude = ln_deg_to_rad(obj.lat)

    ra = atan2((sin(longitude) * cos(nutation.ecliptic) - tan(latitude) * sin(nutation.ecliptic)), cos(longitude))
    declination = sin(latitude) * cos(nutation.ecliptic) + cos(latitude) * sin(nutation.ecliptic)

    pos.ra = ln_range_degrees(ln_rad_to_deg(ra))
    pos.dec = ln_rad_to_deg(declination)


def ln_get_ecl_from_equ(obj, jd, pos):
    nutation = LnNutation
    ra = ln_deg_to_rad(obj.ra)
    declination = ln_deg_to_rad(obj.dec)
    ln_get_nutation(jd, nutation)
    nutation.ecliptic = ln_deg_to_rad(nutation.ecliptic)

    longitude = atan2((sin(ra) * cos(nutation.ecliptic) + tan(declination) * sin(nutation.ecliptic)), cos(ra))
    latitude = sin(declination) * cos(nutation.ecliptic) - cos(declination) * sin(nutation.ecliptic) * sin(ra)
    latitude = asin(latitude)

    pos.lat = ln_rad_to_deg(latitude)
    pos.lng = ln_range_degrees(longitude)


def ln_get_ecl_from_rect(rect, posn):
    t = sqrt(rect.X * rect.X + rect.Y * rect.Y)
    posn.lng = ln_range_degrees(ln_rad_to_deg(atan2(rect.X, rect.Y)))
    posn.lat = ln_rad_to_deg(atan2(t, rect.Z))


def ln_get_equ_from_gal(gal, equ):
    # Transform an object galactic coordinates into B1950 equatorial coordinate.
    rad_27_4 = ln_deg_to_rad(27.4)
    sin_27_4 = sin(rad_27_4)
    cos_27_4 = cos(rad_27_4)

    l_123 = ln_deg_to_rad(gal.l - 123)
    cos_1_123 = cos(l_123)

    rad_gal_b = ln_deg_to_rad(gal.b)

    sin_b = sin(rad_gal_b)
    cos_b = cos(rad_gal_b)

    y = atan2(sin(l_123), cos_1_123 * sin_27_4 - (sin_b / cos_b) * cos_27_4)
    equ.ra = ln_range_degrees(ln_rad_to_deg(y) + 12.25)
    equ.dec = ln_rad_to_deg(asin(sin_b * sin_27_4 + cos_b * cos_27_4 * cos_1_123))


def ln_get_gal_from_equ(equ, gal):
    # Transform an object B1950 equatorial coordinate into galactic coordinates.
    rad_27_4 = ln_deg_to_rad(27.4)
    sin_27_4 = sin(rad_27_4)
    cos_27_4 = cos(rad_27_4)

    ra_192_25 = ln_deg_to_rad(192.25 - equ.ra)
    cos_ra_192_25 = cos(ra_192_25)

    rad_equ_dec = ln_deg_to_rad(equ.dec)

    sin_dec = sin(rad_equ_dec)
    cos_dec = cos(rad_equ_dec)

    x = atan2(sin(ra_192_25), cos_ra_192_25 * sin_27_4 - (sin_dec / cos_dec) * cos_27_4)
    gal.l = ln_range_degrees(303 - ln_rad_to_deg(x))
    gal.b = ln_rad_to_deg(asin(sin_dec * sin_27_4 + cos_dec * cos_27_4 * cos_ra_192_25 ))


def ln_get_equ2000_from_gal(gal, equ):
    ln_get_equ_from_gal(gal, equ)
    ln_get_equ_prec2(equ, B1950, JD2000, equ)

