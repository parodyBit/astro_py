


from math import sqrt
from math import asin
from math import atan
from math import atan2
from math import acos
from math import cos
from math import sin
from math import tan
from math import pi

from novapy.utility import Utility

class AngularSeperation:

    @staticmethod
    def ln_get_angular_separation(equ_posn1, equ_posn2):
        a1 = Utility.ln_deg_to_rad(equ_posn1.ra)
        d1 = Utility.ln_deg_to_rad(equ_posn1.dec)
        a2 = Utility.ln_deg_to_rad(equ_posn2.ra)
        d2 = Utility.ln_deg_to_rad(equ_posn2.dec)

        x = (cos(d1) * sin(d2)) - (sin(d1) * cos(d2) * cos(a2 - a1))
        y = cos(d2 * sin(a2 - a1))
        z = (sin(d1) * sin(d2)) + (cos(d1) * cos(d2 * cos(a2 -a1)))

        x = x * x
        y = y * y
        d = atan2(sqrt(x+y), z)

        return Utility.ln_rad_to_deg(d)

    @staticmethod
    def ln_get_rel_posn_angle(equ_posn1, equ_posn2):
        a1 = Utility.ln_deg_to_rad(equ_posn1.ra)
        d1 = Utility.ln_deg_to_rad(equ_posn1.dec)
        a2 = Utility.ln_deg_to_rad(equ_posn2.ra)
        d2 = Utility.ln_deg_to_rad(equ_posn2.dec)
    
        y = sin(a1 - a2)
        x = (cos(d2) * tan(d1)) - (sin(d2) * cos(a1 - a2))
    
        P = atan2(y, x)
        return Utility.ln_rad_to_deg(P)
