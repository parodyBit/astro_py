

class IGetEquBodyCoords:
    name = ''

    def get_equ_body_coords(self, jd, equ_pos):

        if self.name is not None:
            if self.name == 'solar':
                ln_get_solar_equ_coords(jd, equ_pos)
            elif self.name == 'mercury':
                ln_get_mercury_equ_coords(jd, equ_pos)
            elif self.name == 'venus':
                ln_get_venus_equ_coords()
            elif self.name == 'mars':
                ln_get_mars_equ_coords(jd, equ_pos)
            elif self.name == 'jupiter':
                ln_get_jupiter_equ_coords(jd, equ_pos)
            elif self.name == 'saturn':
                ln_get_saturn_equ_coords(jd, equ_pos)
            elif self.name == 'uranus':
                ln_get_uranus_equ_coords(jd, equ_pos)
            elif self.name == 'neptune':
                ln_get_neptune_equ_coords(jd, equ_pos)
            elif self.name == 'pluto':
                ln_get_pluto_equ_coords(jd, equ_pos)
            elif self.name == 'lunar':
                ln_get_lunar_equ_coords(jd, equ_pos)
            else:
                return

    def set_name(self, name):
        self.name = name


from novapy.solar_system.solar import ln_get_solar_equ_coords
from novapy.solar_system.mercury import ln_get_mercury_equ_coords
from novapy.solar_system.venus import ln_get_venus_equ_coords
from novapy.solar_system.mars import ln_get_mars_equ_coords
from novapy.solar_system.jupiter import ln_get_jupiter_equ_coords
from novapy.solar_system.saturn import ln_get_saturn_equ_coords
from novapy.solar_system.uranus import ln_get_uranus_equ_coords
from novapy.solar_system.neptune import ln_get_neptune_equ_coords
from novapy.solar_system.pluto import ln_get_pluto_equ_coords
from novapy.solar_system.lunar import ln_get_lunar_equ_coords
