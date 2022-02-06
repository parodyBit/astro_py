from novapy.api.ln_equ_posn import LnEquPosn
from novapy.precession import ln_get_equ_prec

from novapy.proper_motion import ln_get_equ_pm
from novapy.abberation import ln_get_equ_aber


def ln_get_apparent_posn(mean_pos, proper_motion, jd, equ_pos):
    proper_posn = LnEquPosn()
    aberration_posn = LnEquPosn()

    ln_get_equ_pm(mean_pos, proper_motion,jd,proper_posn)
    ln_get_equ_aber(proper_posn, jd, aberration_posn)
    ln_get_equ_prec(aberration_posn, jd, equ_pos)

