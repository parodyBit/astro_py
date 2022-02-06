from novapy.api.ln_date import LnDate
from novapy.api.ln_zone_date import LnZoneDate

from novapy.api.ln_equ_posn import LnEquPosn

from novapy.api.ln_rect_posn import LnRectPosn
# for julian test
from novapy.julian_day import ln_get_date
from novapy.julian_day import ln_get_julian_day
from novapy.julian_day import ln_get_day_of_week
from novapy.julian_day import ln_date_to_zonedate
from novapy.julian_day import ln_zonedate_to_date
from novapy.julian_day import ln_get_date_from_sys
from novapy.julian_day import ln_get_julian_from_sys
from novapy.julian_day import ln_get_zonedate_from_sys
# for dynamical test
from novapy.dynamical_time import ln_get_jde
# for heliocentric test
from novapy.heliocentric_time import ln_get_heliocentric_time_diff
#for nutation test
from novapy.nutation import ln_get_nutation
from novapy.api.ln_nutation import LnNutation
# for transform test
from novapy.api.lnh_equ_posn import LnhEquPosn
from novapy.api.ln_lnlat_posn import LnLnlatPosn
from novapy.api.lnh_lnlat_posn import LnhLnlatPosn
from novapy.api.ln_hrz_posn import LnHrzPosn
from novapy.api.ln_gal_posn import LnGalPosn
from novapy.transform import ln_get_hrz_from_equ
from novapy.transform import ln_get_ecl_from_equ
from novapy.transform import ln_get_equ_from_ecl
from novapy.transform import ln_get_equ_from_gal
from novapy.transform import ln_get_gal_from_equ
from novapy.utility import ln_hequ_to_equ
from novapy.utility import ln_hlnlat_to_lnlat
from novapy.utility import ln_lnlat_to_hlnlat
# for sidereal test
from novapy.sidereal_time import ln_get_mean_sidereal_time
from novapy.sidereal_time import ln_get_apparent_sidereal_time
# for solar coord test
from novapy.api.ln_helio_posn import LnHelioPosn
from novapy.solar_system.solar import ln_get_solar_geom_coords
# for aberration test
from novapy.abberation import ln_get_equ_aber
# for precession test
from novapy.precession import ln_get_ecl_prec
from novapy.precession import ln_get_equ_prec
from novapy.precession import ln_get_equ_prec2
from novapy.proper_motion import ln_get_equ_pm
from novapy.api.constants import JD2000
from novapy.api.constants import JD2050
from novapy.api.constants import B1900
# for apparent position test
from novapy.apparent_position import ln_get_apparent_posn
# for vsop87 test
from novapy.solar_system.solar import ln_get_solar_equ_coords
from novapy.solar_system.mercury import ln_get_mercury_helio_coords
from novapy.solar_system.mercury import ln_get_mercury_equ_coords
from novapy.solar_system.mercury import ln_get_mercury_earth_dist
from novapy.solar_system.mercury import ln_get_mercury_solar_dist
from novapy.solar_system.mercury import ln_get_mercury_phase
from novapy.solar_system.mercury import ln_get_mercury_disk
from novapy.solar_system.mercury import ln_get_mercury_magnitude
from novapy.solar_system.mercury import ln_get_mercury_sdiam
from novapy.solar_system.mercury import ln_get_mercury_rst
from novapy.solar_system.mercury import ln_get_mercury_rect_helio
from novapy.solar_system.venus import ln_get_venus_helio_coords
from novapy.solar_system.venus import ln_get_venus_equ_coords
from novapy.solar_system.venus import ln_get_venus_earth_dist
from novapy.solar_system.venus import ln_get_venus_solar_dist
from novapy.solar_system.venus import ln_get_venus_phase
from novapy.solar_system.venus import ln_get_venus_disk
from novapy.solar_system.venus import ln_get_venus_magnitude
from novapy.solar_system.venus import ln_get_venus_sdiam
from novapy.solar_system.mars import ln_get_mars_helio_coords
from novapy.solar_system.mars import ln_get_mars_equ_coords
from novapy.solar_system.mars import ln_get_mars_earth_dist
from novapy.solar_system.mars import ln_get_mars_solar_dist
from novapy.solar_system.mars import ln_get_mars_phase
from novapy.solar_system.mars import ln_get_mars_disk
from novapy.solar_system.mars import ln_get_mars_magnitude
from novapy.solar_system.mars import ln_get_mars_sdiam

from novapy.solar_system.lunar import load_data
from novapy.solar_system.lunar import ln_get_lunar_geo_posn

from novapy.solar_system.jupiter import ln_get_jupiter_helio_coords
from novapy.solar_system.jupiter import ln_get_jupiter_equ_coords
from novapy.solar_system.jupiter import ln_get_jupiter_earth_dist
from novapy.solar_system.jupiter import ln_get_jupiter_solar_dist
from novapy.solar_system.jupiter import ln_get_jupiter_phase
from novapy.solar_system.jupiter import ln_get_jupiter_disk
from novapy.solar_system.jupiter import ln_get_jupiter_magnitude
from novapy.solar_system.jupiter import ln_get_jupiter_equ_sdiam

from novapy.api.ln_lnlat_posn import LnLnlatPosn
from novapy.solar_system.solar import ln_get_solar_rst
from novapy.api.ln_rst_time import LnRstTime
from novapy.julian_day import ln_get_zonedate_from_sys

from novapy.solar_system.saturn import ln_get_saturn_equ_coords
from novapy.solar_system.saturn import ln_get_saturn_helio_coords
from novapy.solar_system.saturn import ln_get_saturn_earth_dist
from novapy.solar_system.saturn import ln_get_saturn_solar_dist
from novapy.solar_system.saturn import ln_get_saturn_magnitude
from novapy.solar_system.saturn import ln_get_saturn_disk
from novapy.solar_system.saturn import ln_get_saturn_phase
from novapy.solar_system.saturn import ln_get_saturn_rst
from novapy.solar_system.saturn import ln_get_saturn_equ_sdiam
from novapy.solar_system.saturn import ln_get_saturn_pol_sdiam
from novapy.solar_system.saturn import ln_get_saturn_rect_helio

from novapy.solar_system.uranus import ln_get_uranus_equ_coords
from novapy.solar_system.uranus import ln_get_uranus_helio_coords
from novapy.solar_system.uranus import ln_get_uranus_earth_dist
from novapy.solar_system.uranus import ln_get_uranus_solar_dist
from novapy.solar_system.uranus import ln_get_uranus_magnitude
from novapy.solar_system.uranus import ln_get_uranus_disk
from novapy.solar_system.uranus import ln_get_uranus_phase
from novapy.solar_system.uranus import ln_get_uranus_rst
from novapy.solar_system.uranus import ln_get_uranus_sdiam
from novapy.solar_system.uranus import ln_get_uranus_rect_helio




from novapy.solar_system.earth import ln_get_earth_solar_dist
from novapy.solar_system.earth import ln_get_earth_helio_coords
from novapy.utility import ln_equ_to_hequ


class Observer:
    position_lnlat = LnLnlatPosn()

    def __init__(self): pass

    def set_position(self, longitude, latitude):
        self.position_lnlat.set_position(longitude, latitude)


class LibNova:
    __instance = None
    observer = Observer()
    current_date = LnDate()
    current_zonedate = LnZoneDate()
    current_julian_date = 0.
    @staticmethod
    def master():
        """ Static access method. """
        if LibNova.__instance is None:
            LibNova()
        return LibNova.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if LibNova.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            LibNova.__instance = self
            self.current_julian_date = ln_get_julian_from_sys()
            ln_get_zonedate_from_sys(self.current_zonedate)
            ln_get_date(self.current_julian_date, self.current_date)


    def set_observer_lat_lng(self, lat, lng):
        self.observer.lng = lng
        self.observer.lat = lat



class Planet:
    name = ''
    position_hel = LnHelioPosn()
    position_equ = LnEquPosn()

    def __init__(self):pass


class Solar:
    position = LnEquPosn()


class Lunar: pass
