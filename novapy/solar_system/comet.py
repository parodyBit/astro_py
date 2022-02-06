from novapy.elliptic_motion import ln_get_ell_mean_motion
from novapy.elliptic_motion import ln_get_ell_mean_anomaly
from novapy.elliptic_motion import ln_get_ell_radius_vector
from novapy.elliptic_motion import ln_get_ell_body_solar_dist
from novapy.elliptic_motion import ln_solve_kepler
from novapy.parabolic_motion import ln_get_par_radius_vector
from novapy.parabolic_motion import ln_get_par_body_solar_dist
from math import log10


def ln_get_ell_comet_mag(jd, ell_orbit, g, k):
    if ell_orbit.n == 0:
        ell_orbit.n = ln_get_ell_mean_motion(ell_orbit.a)
    m = ln_get_ell_mean_anomaly(ell_orbit.n, jd - ell_orbit.jd)
    e = ln_solve_kepler(ell_orbit.e, m)
    r = ln_get_ell_radius_vector(ell_orbit.a, ell_orbit.e, e)
    d = ln_get_ell_body_solar_dist(jd, ell_orbit)
    return g + 5.0 * log10(d) + k * log10(r)


def ln_get_par_comet_mag(jd, par_orbit, g, k):
    t = jd - par_orbit.jd
    r = ln_get_par_radius_vector(par_orbit.q, t)
    d = ln_get_par_body_solar_dist(jd, par_orbit)
    return g + 5.0 * log10(d) + k * log10(r)
