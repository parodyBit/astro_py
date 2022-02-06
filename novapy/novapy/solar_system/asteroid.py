from novapy.api.ln_ell_orbit import LnEllOrbit
from math import log10
from math import exp
from math import pow
from math import tan
from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_range_degrees
from novapy.elliptic_motion import ln_get_ell_body_phase_angle
from novapy.elliptic_motion import ln_get_ell_mean_motion
from novapy.elliptic_motion import ln_get_ell_mean_anomaly
from novapy.elliptic_motion import ln_get_ell_radius_vector
from novapy.elliptic_motion import ln_get_ell_body_solar_dist
from novapy.elliptic_motion import ln_get_ell_body_earth_dist
from novapy.elliptic_motion import ln_solve_kepler

def ln_get_asteroid_mag(jd, ell_orbit, h, g):
    b = ln_get_ell_body_phase_angle(jd, ell_orbit)
    b = ln_deg_to_rad(b)
    if ell_orbit.n == 0:
        ell_orbit.n = ln_get_ell_mean_motion(ell_orbit.a)
    m = ln_get_ell_mean_anomaly(ell_orbit.n, jd - ell_orbit.jd)
    e = ln_solve_kepler(ell_orbit.e, m)
    r = ln_get_ell_radius_vector(ell_orbit.a, ell_orbit.e, e)
    d = ln_get_ell_body_solar_dist(jd, ell_orbit)
    t1 = exp(-3.33 * pow(tan(b / 2.0), 0.63))
    t2 = exp(-0.187 * pow(tan(b / 2.0), 1.22))
    return h + 5.0 * log10(r * d) - 2.5 * log10((1.0 - g) * t1 + g * t2)



def ln_get_asteroid_sdiam_km(h, a):
    '''
    Calculate the semidiameter of an asteroid in km.
        Note: Many asteroids have an irregular shape and therefore this function
	    returns an approximate value of the diameter.
    '''
    return 3.13 - 0.2 * h - (0.5 * log10(a))


def ln_get_asteroid_sdiam_arc(jd, ell_orbit, h, a):
    '''
    ln_get_asteroid_sdiam_arc(jd, ell_orbit, h, a)
    jd = julian day
    ell_orbit = orbital parameters
    h = absolute magnitude of asteroid
    a = albedo of asteroid
    returns: semidiameter in seconds of arc
    Calculate the semidiameter of an asteroid
        Note: Manye asteroids have an irregular shape and therefore
        this function returns an approximate value of the diameter

    '''
    dist = ln_get_ell_body_earth_dist(jd, ell_orbit)
    d = 3.13 - 0.2 * h - (0.5 * log10(a))
    return 0.0013788 * d / dist
