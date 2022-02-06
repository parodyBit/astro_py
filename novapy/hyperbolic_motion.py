

from novapy.utility import cbrt

from novapy.solar_system.solar import LN_SOLAR_STANDARD_HORIZON

from math import sqrt
from math import atan
from math import atan2
from math import acos
from math import cos
from math import sin
from math import tan

from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_range_degrees
from novapy.utility import nan
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





GAUS_GRAV = 0.01720209895
PREC = 0.0000000001



def ln_solve_hyp_barker(q1, g, t):
    q2 = q1 * t
    s = 2 / (3 * abs(q2))
    s = 2 / tan(2 * atan(cbrt(tan(atan(s) / 2))))

    if t < 0:
        s = -1 * s
    l = 0

    while True:
        # break if abs(s1 - s0) < precision default:1e-10
        s0 = s
        z = 1
        y = s * s
        g1 = (-1 * y) * s
        q3 = q2 + 2.0 * g * s * y / 3.0

        while True:
            # break if abs(f) < precision default:1e-10
            z += 1
            g1 = (-1 * g1) * g * y
            z1 = (z - (z + 1) * g) / (2.0 * z + 1.0)
            f = z1 * g1
            q3 = q3 + f

            if z > 100 or abs(f) > 10000:
                return nan('0')
            if abs(f) < PREC:
                break

        l += 1
        if l > 100:
            return nan('0')

        while True:
            s1 = s
            s = (2 * s * s * s / 3 + q3) / (s * s + 1)
            if abs(s - s1) < PREC:
                break


        if abs(s - s0) < PREC:
            break
    return s


def ln_get_hyp_true_anomaly(q, e, t):
    Q = (GAUS_GRAV / (2.0 * q)) * sqrt((1.0 + e) / q)
    gama = (1.0 - e) / (1.0 + e)

    s = ln_solve_hyp_barker(Q, gama, t)
    v = 2.0 * atan(s)

    return ln_range_degrees((ln_rad_to_deg(v)))


def ln_get_hyp_radius_vector(q, e, t):
    i = cos(ln_deg_to_rad(ln_get_hyp_true_anomaly(q, e, t)))
    return q * (1.0 + e) / (1.0 + e * i)


def ln_get_hyp_helio_rect_posn(orbit, jd, rect_posn):
    t = jd - orbit.jd

    # J2000 obliquity of the ecliptic
    sin_e = 0.397777156
    cos_e = 0.917482062

    #  equ 33.7 
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
    
    # equ 33.8 */
    A = atan2(F, P)
    B = atan2(G, Q)
    C = atan2(H, R)
    a = sqrt(F * F + P * P)
    b = sqrt(G * G + Q * Q)
    c = sqrt(H * H + R * R)

    # get true anomaly 
    v = ln_get_hyp_true_anomaly(orbit.q, orbit.e, t)

    # get radius vector 
    r = ln_get_hyp_radius_vector(orbit.q, orbit.e, t)

    # /** equ 33.9 */
    rect_posn.x = r * a * sin(A + ln_deg_to_rad(orbit.w + v))
    rect_posn.y = r * b * sin(B + ln_deg_to_rad(orbit.w + v))
    rect_posn.z = r * c * sin(C + ln_deg_to_rad(orbit.w + v))


def ln_get_hyp_geo_rect_posn(orbit, jd, rect_posn):
    p_posn = LnRectPosn()
    e_posn = LnRectPosn()
    earth = LnHelioPosn()

    ln_get_hyp_helio_rect_posn(orbit, jd, p_posn)
    ln_get_earth_helio_coords(jd, earth)
    ln_get_rect_from_helio(earth, e_posn)

    rect_posn.x = p_posn.x - e_posn.x
    rect_posn.y = p_posn.y - e_posn.y
    rect_posn.z = p_posn.z - e_posn.z





def ln_get_hyp_body_equ_coords(jd, orbit, equ_posn):
    body_rect_posn = LnRectPosn()
    sol_rect_posn = LnRectPosn()

    ln_get_hyp_helio_rect_posn(orbit, jd, body_rect_posn)
    ln_get_solar_geo_coords(jd, sol_rect_posn)

    dist = ln_get_rect_distance(body_rect_posn, sol_rect_posn)
    t = ln_get_light_time(dist)

    ln_get_hyp_helio_rect_posn(orbit, jd - t, body_rect_posn)

    x = sol_rect_posn.x + body_rect_posn.x
    y = sol_rect_posn.y + sol_rect_posn.y
    z = sol_rect_posn.z + sol_rect_posn.z

    equ_posn.ra = ln_range_degrees(ln_rad_to_deg(atan2(y, x)))
    equ_posn.dec = ln_rad_to_deg(atan2(z, sqrt(x * x + y * y)))


def ln_get_hyp_body_earth_dist(jd, orbit):
    body_rect_pos = LnRectPosn()
    earth_rect_pos = LnRectPosn()
    ln_get_hyp_geo_rect_posn(orbit,jd,body_rect_pos)
    earth_rect_pos.x = 0.0
    earth_rect_pos.y = 0.0
    earth_rect_pos.z = 0.0
    return ln_get_rect_distance(body_rect_pos,earth_rect_pos)


def ln_get_hyp_body_solar_dist(jd, orbit):
    body_rect_pos = LnRectPosn()
    sol_rect_pos = LnRectPosn()
    ln_get_hyp_helio_rect_posn(orbit, jd, body_rect_pos)
    sol_rect_pos.x = 0.0
    sol_rect_pos.y = 0.0
    sol_rect_pos.z = 0.0
    return ln_get_rect_distance(body_rect_pos,sol_rect_pos)


def ln_get_hyp_body_phase_angle(jd, orbit):
    t = jd - orbit.jd
    r = ln_get_hyp_radius_vector(orbit.q, orbit.e, t)
    R = ln_get_earth_solar_dist(jd)
    d = ln_get_hyp_body_solar_dist(jd, orbit)
    phase = (r * r + d * d - R * R) / (2.0 * r * d)
    return ln_range_degrees(ln_rad_to_deg(acos(phase)))


def ln_get_hyp_body_elong(jd, orbit):
    t = jd - orbit.jd
    r = ln_get_hyp_radius_vector(orbit.q, orbit.e, t)
    R = ln_get_earth_solar_dist(jd)
    d = ln_get_hyp_body_solar_dist(jd, orbit)
    elong = (R * R + d * d - r * r) / (2.0 * R * d)
    return ln_range_degrees(ln_rad_to_deg(acos(elong)))


def ln_get_hyp_body_rst(jd, obs, orbit, rst):
    motion_coords = IGetMotionBodyCoords()
    motion_coords.set_name('hyperbolic')

    return ln_get_motion_body_rst_horizon(jd,obs,motion_coords,orbit, LN_SOLAR_STANDARD_HORIZON, rst)


def ln_get_hyp_body_rst_horizon(jd, obs, motion_coords, orbit, horizon, rst):
    return ln_get_motion_body_rst_horizon(jd, obs, motion_coords, orbit, horizon, rst)


def ln_get_hyp_body_next_rst(jd, obs, orbit, rst):
    return ln_get_hyp_body_next_rst_horizon(jd, obs, orbit, LN_SOLAR_STANDARD_HORIZON, rst)


def ln_get_hyp_body_next_rst_horizon(jd, obs, orbit, horizon, rst):
    motion_coords = IGetMotionBodyCoords()
    motion_coords.set_name('hyperbolic')

    return ln_get_motion_body_next_rst_horizon(jd, obs, motion_coords,orbit, horizon, rst)


def ln_get_hyp_body_next_rst_horizon_future(jd, obs, orbit, horizon, day_limit, rst):
    motion_coords = IGetMotionBodyCoords()
    motion_coords.set_name('hyperbolic')

    return ln_get_motion_body_next_rst_horizon_future(jd, obs, motion_coords, orbit, horizon, day_limit, rst)


from novapy.util.i_get_motion_body_coords import IGetMotionBodyCoords
