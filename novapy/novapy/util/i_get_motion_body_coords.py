
class IGetMotionBodyCoords:
    name = ''

    def set_name(self, name):
        self.name = name

    def get_motion_body_coords(self, jd, orbit, equ_pos):
        if self.name is not None:
            if self.name == 'hyperbolic':
                ln_get_hyp_body_equ_coords(jd, orbit, equ_pos)
            elif self.name == 'elliptic':
                ln_get_ell_body_equ_coords(jd, orbit, equ_pos)
            elif self.name == 'parabolic':
                ln_get_par_body_equ_coords(jd, orbit, equ_pos)


from novapy.hyperbolic_motion import ln_get_hyp_body_equ_coords
from novapy.elliptic_motion import ln_get_ell_body_equ_coords
from novapy.parabolic_motion import ln_get_par_body_equ_coords