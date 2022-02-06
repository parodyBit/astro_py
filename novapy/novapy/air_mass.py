from math import asin
from math import sin
from math import sqrt

from novapy.utility import Utility


class Airmass:

    @staticmethod
    def ln_get_airmass(alt, airmass_scale):
        a = airmass_scale * sin(Utility.ln_deg_to_rad(alt))
        return sqrt(a * a + 2 * airmass_scale + 1) - a

    @staticmethod
    def ln_get_alt_from_airmass(x, airmass_scale):
        return Utility.ln_rad_to_deg(asin((2 * airmass_scale + 1 - x * x) / (2 * x * airmass_scale)))
