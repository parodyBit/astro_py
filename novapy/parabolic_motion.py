

from novapy.utility import cbrt

from novapy.solar_system.solar import LN_SOLAR_STANDARD_HORIZON

from math import sqrt
from math import atan
from math import atan2
from math import acos
from math import cos
from math import sin

from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_range_degrees

from novapy.utility import ln_get_rect_distance
from novapy.utility import ln_get_light_time
from novapy.transform import ln_get_rect_from_helio
from novapy.riseset import ln_get_motion_body_rst_horizon
from novapy.riseset import ln_get_motion_body_next_rst_horizon_future
from novapy.riseset import ln_get_motion_body_next_rst_horizon

from novapy.api.ln_rect_posn import LnRectPosn
from novapy.api.ln_helio_posn import LnHelioPosn
from novapy.solar_system.earth import ln_get_earth_solar_dist
from novapy.solar_system.earth import ln_get_earth_helio_coords

from novapy.solar_system.solar import ln_get_solar_geo_coords





def ln_solve_barker(q, t):
    w = ((0.03649116245) / (q * sqrt(q))) * t
    g = w / 2.0
    y = cbrt(g + sqrt(g * g + 1.0))
    return y - 1.0 / y


def ln_get_par_true_anomaly(q, t):
    s = ln_solve_barker(q, t)
    v = 2.0 * atan(s)
    return ln_range_degrees(ln_rad_to_deg(v))


def ln_get_par_radius_vector(q, t):
    s = ln_solve_barker(q, t)
    return q * (1.0 + s * s)


def ln_get_par_helio_rect_posn(orbit, jd, posn):
    t = jd - orbit.jd

    sin_e = 0.397777156
    cos_e = 0.917482062

    sin_omega = sin(ln_deg_to_rad(orbit.omega))
    cos_omega = cos(ln_deg_to_rad(orbit.omega))
    sin_i = sin(ln_deg_to_rad(orbit.i))
    cos_i = cos(ln_deg_to_rad(orbit.i))
    f = cos_omega
    g = sin_omega * cos_e
    h = sin_omega * sin_e
    p = (-1*sin_omega) * cos_i
    q = cos_omega * cos_i * cos_e - sin_i * sin_e
    r = cos_omega * cos_i * sin_i + sin_i * cos_e

    A = atan2(f, p)
    B = atan2(g, q)
    C = atan2(h, r)
    a = sqrt(f * f + p * p)
    b = sqrt(g * g + q * q)
    c = sqrt(h * h + r * r)

    v = ln_get_par_true_anomaly(orbit.q, t)
    r = ln_get_par_radius_vector(orbit.q, t)

    posn.x = r * a * sin(A + ln_deg_to_rad(orbit.w + v))
    posn.y = r * b * sin(B + ln_deg_to_rad(orbit.w + v))
    posn.z = r * c * sin(C + ln_deg_to_rad(orbit.w + v))


def ln_get_par_geo_rect_posn(orbit, jd, rect_posn):
    p_posn = LnRectPosn()
    e_posn = LnRectPosn()
    earth = LnHelioPosn()

    ln_get_par_helio_rect_posn(orbit, jd, p_posn)
    ln_get_earth_helio_coords(jd, earth)
    ln_get_rect_from_helio(earth, e_posn)
    rect_posn.x = p_posn.x - e_posn.x
    rect_posn.y = p_posn.y - e_posn.y
    rect_posn.z = p_posn.z - e_posn.z


def ln_get_par_body_equ_coords(jd, par_orbit, equ_posn):
    body_rect_posn = LnRectPosn()
    sol_rect_posn = LnRectPosn()
    ln_get_par_helio_rect_posn(par_orbit, jd, body_rect_posn)
    ln_get_solar_geo_coords(jd, sol_rect_posn)
    dist = ln_get_rect_distance(body_rect_posn, sol_rect_posn)
    t = ln_get_light_time(dist)
    ln_get_par_helio_rect_posn(par_orbit, jd - t, body_rect_posn)
    x = sol_rect_posn.x + body_rect_posn.x
    y = sol_rect_posn.y + body_rect_posn.y
    z = sol_rect_posn.z + body_rect_posn.z

    equ_posn.ra = ln_range_degrees(ln_rad_to_deg(atan2(y, x)))
    equ_posn.dec = ln_rad_to_deg(atan2(z, sqrt(x * x + y * y)))

def ln_get_par_body_earth_dist(jd, par_orbit):
    body_rect_posn = LnRectPosn()
    earth_rect_posn = LnRectPosn()
    ln_get_par_geo_rect_posn(par_orbit, jd, body_rect_posn)
    earth_rect_posn.x = 0
    earth_rect_posn.y = 0
    earth_rect_posn.z = 0
    return ln_get_rect_distance(body_rect_posn, earth_rect_posn)

def ln_get_par_body_solar_dist(jd, par_orbit):
    body_rect_posn = LnRectPosn()
    sol_rect_posn = LnRectPosn()
    ln_get_par_helio_rect_posn(par_orbit, jd, body_rect_posn)
    sol_rect_posn.x = 0
    sol_rect_posn.y = 0
    sol_rect_posn.z = 0
    return ln_get_rect_distance(body_rect_posn, sol_rect_posn)

def ln_get_par_body_phase_angle(jd, par_orbit):
    t = jd - par_orbit.jd
    r = ln_get_par_radius_vector(par_orbit.q, t)
    R = ln_get_earth_solar_dist(jd)
    d = ln_get_par_body_solar_dist(jd, par_orbit)
    phase = (r * r + d * d - R * R) / (2.0 * r * d)
    return ln_range_degrees(ln_rad_to_deg(acos(phase)))

def ln_get_par_body_elong(jd, par_orbit):
    t = jd - par_orbit.jd
    r = ln_get_par_radius_vector(par_orbit.q, t)
    R = ln_get_earth_solar_dist(jd)
    d = ln_get_par_body_solar_dist(jd, par_orbit)
    elong = (R * R + d * d - r * r) / (2.0 * R * d)
    return ln_range_degrees(ln_rad_to_deg(acos(elong)))

def ln_get_par_body_rst(jd, obs, par_orbit, rst):
    return ln_get_par_body_rst_horizon(jd, obs, par_orbit, LN_SOLAR_STANDARD_HORIZON, rst)


def ln_get_par_body_rst_horizon(jd, obs, par_orbit, horizon, rst):
    body_coords = IGetMotionBodyCoords()
    body_coords.set_name('parabolic')
    return ln_get_motion_body_rst_horizon(jd, obs, body_coords,par_orbit, horizon, rst)

def ln_get_par_body_next_rst(jd, obs, par_orbit, rst):
    return ln_get_par_body_next_rst_horizon(jd, obs, par_orbit, LN_SOLAR_STANDARD_HORIZON, rst)

def ln_get_par_body_next_rst_horizon(jd, obs, par_orbit, horizon, rst):
    body_coords = IGetMotionBodyCoords()
    body_coords.set_name('parabolic')
    return ln_get_motion_body_next_rst_horizon(jd, obs, body_coords, par_orbit, horizon, rst)

def ln_get_par_body_next_rst_horizon_future(jd, obs, par_orbit, horizon, day_limit, rst):
    body_coords = IGetMotionBodyCoords()
    body_coords.set_name('parabolic')
    return ln_get_motion_body_next_rst_horizon_future(jd, obs, body_coords, par_orbit, horizon, day_limit, rst)

from novapy.util.i_get_motion_body_coords import IGetMotionBodyCoords