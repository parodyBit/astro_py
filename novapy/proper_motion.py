from novapy.utility import ln_range_degrees
from novapy.api.constants import JD2000


def ln_get_equ_pm(mean_pos, proper_motion, jd, pos):
    return ln_get_equ_pm_epoch(mean_pos, proper_motion, jd, JD2000, pos)


def ln_get_equ_pm_epoch(mean_pos, proper_motion, jd, epoch_jd, pos):
    t = (jd - epoch_jd) / 365.25
    pos.ra = mean_pos.ra + t * proper_motion.ra
    pos.dec = mean_pos.dec + t * proper_motion.dec
    pos.ra = ln_range_degrees(pos.ra)
