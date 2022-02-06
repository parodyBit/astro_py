from math import atan
from math import atan2
from math import cos
from math import sin
from math import tan
from math import pi

from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg
from novapy.api.value_ref import ValueRef

def get_topocentric(obs, height, ro_sin, ro_cos):
    lat_rad = ln_deg_to_rad(obs.lat)
    u = atan(0.99664719 * tan(lat_rad))
    ro_sin = 0.99664719 * sin(u) + (height / 6378140) * sin(lat_rad)
    ro_cos = cos(u) + (height / 6378140) * cos(lat_rad)

    if obs.lat > 0:
        ro_sin.value = abs(ro_sin)
    else:
        ro_sin.value = abs(ro_sin) * -1
    ro_cos.value = abs(ro_cos)


def ln_get_parallax(obj, au_dist, obs, height, jd, parallax):
    ro_sin = ValueRef()
    ro_cos = ValueRef()
    h = float()
    get_topocentric(obs, height, ro_sin, ro_cos)
    sin_pi = sin(ln_deg_to_rad((8.794 / au_dist) / 3600.0))

    h *= pi / 12.0
    sin_h = sin(h)
    cos_h = cos(h)

    dec_rad = ln_deg_to_rad(obj.dec)
    cos_dec = cos(dec_rad)

    parallax.ra = atan2((-1.0 * ro_cos.value)*sin_pi * sin_h, cos_dec - ro_cos.value * sin_pi * cos_h)
    parallax.dec = atan2((sin(dec_rad) - ro_sin.value * sin_pi) * cos(parallax.ra),
                         cos_dec - ro_cos.value * sin_pi * cos_h)

    parallax.ra = ln_rad_to_deg(parallax.ra)
    parallax.dec = ln_rad_to_deg(parallax.dec)


def ln_get_parallax_ha(obj, au_distance, obs, height, H, parallax):
    ro_sin = ValueRef()
    ro_cos = ValueRef()

    get_topocentric(obs, height, ro_sin, ro_cos)
    sin_pi = sin(ln_deg_to_rad((8.794 / au_distance) / 3600.0))

    H *= pi / 12.0

    sin_H = sin(H)
    cos_H = cos(H)

    dec_rad = ln_deg_to_rad(obj.dec)
    cos_dec = cos(dec_rad)

    parallax.ra = atan2(-ro_cos.value * sin_pi * sin_H,
                        cos_dec - ro_cos.value * sin_pi * cos_H)
    parallax.dec = atan2((sin(dec_rad) - ro_sin.value * sin_pi) * cos(parallax.ra),
                         cos_dec - ro_cos.value * sin_pi * cos_H)

    parallax.ra = ln_rad_to_deg(parallax.ra)
    parallax.dec = ln_rad_to_deg(parallax.dec) - obj.dec
