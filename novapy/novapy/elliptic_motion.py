from novapy.api.constants import M_PI
from novapy.api.constants import M_PI_2
from novapy.api.constants import M_PI_4
from novapy.solar_system.solar import LN_SOLAR_STANDARD_HORIZON

from novapy.utility import Utility

from math import sqrt
from math import asin
from math import atan
from math import atan2
from math import acos
from math import cos
from math import sin
from math import tan
from math import pi

from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_range_degrees

from novapy.utility import ln_get_rect_distance
from novapy.utility import ln_get_light_time
from novapy.transform import ln_get_rect_from_helio
from novapy.riseset import ln_get_motion_body_rst_horizon
from novapy.riseset import ln_get_motion_body_next_rst_horizon
from novapy.riseset import ln_get_motion_body_next_rst_horizon_future

from novapy.api.ln_rect_posn import LnRectPosn
from novapy.api.ln_helio_posn import LnHelioPosn
from novapy.solar_system.earth import ln_get_earth_solar_dist
from novapy.solar_system.earth import ln_get_earth_helio_coords

from novapy.solar_system.solar import ln_get_solar_geo_coords




KEPLER_STEPS = 53


def sgn(x):
    if x == 0.0:
        return x
    elif x < 0.0:
        return -1.0
    else:
        return 1.0



def ln_solve_kepler(e, M):

    Eo = M_PI_2
    D = M_PI_4

    M = ln_deg_to_rad(M)

    F = sgn(M)
    M = abs(M) / (2.0 * pi)
    M = (M - int(M)) * 2.0 * pi * F

    if M < 0:
        M = M + 2.0 * pi
    if M > pi:
        F = -1.0
    if M > pi:
        M = 2.0 * pi - M

    i = 0
    while True:
        M1 = Eo - e * sin(Eo)
        Eo = Eo + D * sgn(M - M1)
        D /= 2.0
        i += 1
        if i > KEPLER_STEPS:
            break

    Eo *= F
    Eo = ln_rad_to_deg(Eo)
    return Eo


def ln_get_ell_mean_anomaly(n, delta_jd):
    return delta_jd * n


def ln_get_ell_true_anomaly(e, E):
    E = ln_deg_to_rad(E)
    v = sqrt((1.0 + e) / (1.0 - e)) * tan(E / 2.0)
    v = 2.0 * atan(v)
    v = ln_range_degrees(ln_rad_to_deg(v))
    return v


def ln_get_ell_radius_vector(a, e, E):
    return a * (1.0 - e * cos(ln_deg_to_rad(E)))


def ln_get_ell_smajor_diam(e, q):
    return q / (1.0 - e)


def ln_get_ell_sminor_diam(e, a):
    return a * sqrt(1 - e * e)


def ln_get_ell_mean_motion(a):
    q = 0.9856076686
    # Gaussian gravitational constant (degrees)
    return q / (a * sqrt(a))


def ln_get_ell_helio_rect_posn(orbit, jd, rect_posn):
    sin_e = 0.397777156
    cos_e = 0.917482062

    sin_omega = sin(ln_deg_to_rad(orbit.omega))
    cos_omega = cos(ln_deg_to_rad(orbit.omega))
    sin_i = sin(ln_deg_to_rad(orbit.i))
    cos_i = cos(ln_deg_to_rad(orbit.i))
    F = cos_omega
    G = sin_omega * cos_e
    H = sin_omega * sin_e
    P = -sin_omega * cos_i
    Q = cos_omega * cos_i * cos_e - sin_i * sin_e
    R = cos_omega * cos_i * sin_e + sin_i * cos_e

    A = atan2(F, P)
    B = atan2(G, Q)
    C = atan2(H, R)
    a = sqrt(F * F + P * P)
    b = sqrt(G * G + Q * Q)
    c = sqrt(H * H + R * R)

    # daily motion
    if orbit.n == 0.0:
        orbit.n = ln_get_ell_mean_motion(orbit.a)

    # mean anomaly
    M = ln_get_ell_mean_anomaly(orbit.n, jd - orbit.jd)

    # eccentric anomaly
    E = ln_solve_kepler(orbit.e, M)

    # get true anomaly
    v = ln_get_ell_true_anomaly(orbit.e, E)

    # radius vector
    r = ln_get_ell_radius_vector(orbit.a, orbit.e, E)

    rect_posn.x = r * a * sin(A + ln_deg_to_rad(orbit.w + v))
    rect_posn.y = r * b * sin(B + ln_deg_to_rad(orbit.w + v))
    rect_posn.z = r * c * sin(B + ln_deg_to_rad(orbit.w + v))



def ln_get_ell_geo_rect_posn(orbit, jd, rect_posn):
    p_pos = LnRectPosn()
    e_pos = LnRectPosn()
    earth = LnHelioPosn()

    ln_get_ell_geo_rect_posn(orbit, jd, p_pos)

    ln_get_earth_helio_coords(jd, earth)

    ln_get_rect_from_helio(earth, e_pos)

    rect_posn.x = e_pos.x - p_pos.x
    rect_posn.y = e_pos.y - p_pos.y
    rect_posn.z = e_pos.z - p_pos.z



def ln_get_ell_body_equ_coords(jd, orbit, equ_posn):
    body_rect_posn = LnRectPosn()
    sol_rect_posn = LnRectPosn()

    ln_get_ell_helio_rect_posn(orbit, jd, body_rect_posn)
    ln_get_solar_geo_coords(jd, sol_rect_posn)

    dist = ln_get_rect_distance(body_rect_posn, sol_rect_posn)
    t = ln_get_light_time(dist)

    ln_get_ell_helio_rect_posn(orbit, jd - t, body_rect_posn)

    x = sol_rect_posn.x + body_rect_posn.x
    y = sol_rect_posn.y + body_rect_posn.y
    z = sol_rect_posn.z + body_rect_posn.z

    equ_posn.ra = ln_range_degrees(ln_rad_to_deg(atan2(y, x)))
    equ_posn.dec = ln_rad_to_deg(asin(z / sqrt(x * x + y * y + z * z)))



def ln_get_ell_orbit_len(orbit):
    b = ln_get_ell_sminor_diam(orbit.e, orbit.a)
    A = (orbit.a + b) / 2.0
    G = sqrt(orbit.a * b)
    H = (2.0 * orbit.a * b) / (orbit.a + b)

    return pi * ((21.0 * A - 2.0 * G - 3.0 * H) / 8.0)


def ln_get_ell_orbit_vel(jd, orbit):
    r = ln_get_ell_body_solar_dist(jd, orbit)
    V = 1.0 / r - 1.0 / (2.0 * orbit.a)
    V = 42.1219 * sqrt(V)
    return V


def ln_get_ell_orbit_pvel(orbit):
    V = 29.7847 / sqrt(orbit.a)
    V *= sqrt((1.0 + orbit.e) / (1.0 - orbit.e))
    return V


def ln_get_ell_orbit_avel(orbit):
    V = 29.7847 / sqrt(orbit.a)
    V *= sqrt((1.0 - orbit.e) / (1.0 + orbit.e))
    return V


def ln_get_ell_body_solar_dist(jd, orbit):
    body_rect_posn = LnRectPosn()
    sol_rec_posn = LnRectPosn()

    ln_get_ell_helio_rect_posn(orbit, jd, body_rect_posn)
    sol_rec_posn.x = 0.0
    sol_rec_posn.y = 0.0
    sol_rec_posn.z = 0.0

    return ln_get_rect_distance(body_rect_posn, sol_rec_posn)


def ln_get_ell_body_earth_dist(jd, orbit):
    body_rect_posn = LnRectPosn()
    earth_rec_posn = LnRectPosn()

    ln_get_ell_geo_rect_posn(orbit, jd, body_rect_posn)
    earth_rec_posn.x = 0.0
    earth_rec_posn.y = 0.0
    earth_rec_posn.z = 0.0

    return ln_get_rect_distance(body_rect_posn, earth_rec_posn)


def ln_get_ell_body_phase_angle(jd, orbit):

    if orbit.n == 0.0:
        orbit.n = ln_get_ell_mean_motion(orbit.a)
    M = ln_get_ell_mean_anomaly(orbit.n, jd - orbit.jd)

    E = ln_solve_kepler(orbit.e, M)
    r = ln_get_ell_radius_vector(orbit.a, orbit.e, E)
    R = ln_get_ell_body_earth_dist(jd, orbit)
    d = ln_get_ell_body_solar_dist(jd, orbit)
    phase = (r * r + d * d - R * R) / (2.0 * r * d)
    return ln_range_degrees(acos(ln_deg_to_rad(phase)))


def ln_get_ell_body_elong(jd, orbit):
    t = jd - orbit.jd
    if orbit.n == 0.0:
        orbit.n = ln_get_ell_mean_motion(orbit.a)
    M = ln_get_ell_mean_anomaly(orbit.n, jd - orbit.jd)

    E = ln_solve_kepler(orbit.e, M)
    r = ln_get_ell_radius_vector(orbit.a, orbit.e, E)

    R = ln_get_earth_solar_dist(jd)
    d = ln_get_ell_body_solar_dist(jd, orbit)

    elong = ( R * R + d * d - r * r) / (2.0 * R * d)
    return ln_range_degrees(ln_rad_to_deg(acos(elong)))



def ln_get_ell_body_rst(jd, obs, orbit, rst):
    return ln_get_ell_body_rst_horizon(jd, obs, orbit, LN_SOLAR_STANDARD_HORIZON, rst)


def ln_get_ell_body_rst_horizon(jd, obs, orbit, horizon, rst):
    motion_coords = IGetMotionBodyCoords()
    motion_coords.set_name('elliptic')
    return ln_get_motion_body_rst_horizon(jd, obs, motion_coords, orbit, horizon, rst)


def ln_get_ell_body_next_rst(jd, obs, orbit, rst):
    return ln_get_ell_body_next_rst_horizon(jd, obs, orbit, LN_SOLAR_STANDARD_HORIZON, rst)


def ln_get_ell_body_next_rst_horizon(jd, obs, orbit, horizon, rst):
    motion_coords = IGetMotionBodyCoords()
    motion_coords.set_name('elliptic')
    return ln_get_motion_body_next_rst_horizon(jd, obs, motion_coords, orbit, horizon, rst)


def ln_get_ell_body_next_rst_horizon_future(jd, obs, orbit, horizon,day_limit, rst):
    motion_coords = IGetMotionBodyCoords()
    motion_coords.set_name('elliptic')
    return ln_get_motion_body_next_rst_horizon_future(jd, obs, motion_coords, orbit, horizon, day_limit, rst)


def ln_get_ell_last_perihelion(epoch_jd, M, n):
    return epoch_jd - (M / n)


from novapy.util.i_get_motion_body_coords import IGetMotionBodyCoords
