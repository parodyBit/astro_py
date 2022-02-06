from nova.novapy.api.ln_date import LnDate
from nova.novapy.api.ln_zone_date import LnZoneDate

from nova.novapy.api.ln_equ_posn import LnEquPosn

from nova.novapy.api.ln_rect_posn import LnRectPosn
# for julian test
from nova.novapy.julian_day import ln_get_date
from nova.novapy.julian_day import ln_get_julian_day
from nova.novapy.julian_day import ln_get_day_of_week
from nova.novapy.julian_day import ln_date_to_zonedate
from nova.novapy.julian_day import ln_zonedate_to_date
from nova.novapy.julian_day import ln_get_date_from_sys
from nova.novapy.julian_day import ln_get_julian_from_sys
from nova.novapy.julian_day import ln_get_zonedate_from_sys
# for dynamical test
from nova.novapy.dynamical_time import ln_get_jde
# for heliocentric test
from nova.novapy.heliocentric_time import ln_get_heliocentric_time_diff
# for nutation test
from nova.novapy.nutation import ln_get_nutation
from nova.novapy.api.ln_nutation import LnNutation
# for transform test
from nova.novapy.api.lnh_equ_posn import LnhEquPosn
from nova.novapy.api.ln_lnlat_posn import LnLnlatPosn
from nova.novapy.api.lnh_lnlat_posn import LnhLnlatPosn
from nova.novapy.api.ln_hrz_posn import LnHrzPosn
from nova.novapy.api.ln_gal_posn import LnGalPosn
from nova.novapy.transform import ln_get_hrz_from_equ
from nova.novapy.transform import ln_get_ecl_from_equ
from nova.novapy.transform import ln_get_equ_from_ecl
from nova.novapy.transform import ln_get_equ_from_gal
from nova.novapy.transform import ln_get_gal_from_equ
from nova.novapy.utility import ln_hequ_to_equ
from nova.novapy.utility import ln_hlnlat_to_lnlat
from nova.novapy.utility import ln_lnlat_to_hlnlat
# for sidereal test
from nova.novapy.sidereal_time import ln_get_mean_sidereal_time
from nova.novapy.sidereal_time import ln_get_apparent_sidereal_time
# for solar coord test
from nova.novapy.api.ln_helio_posn import LnHelioPosn
from nova.novapy.solar_system.solar import ln_get_solar_geom_coords
# for aberration test
from nova.novapy.abberation import ln_get_equ_aber
# for precession test
from nova.novapy.precession import ln_get_ecl_prec
from nova.novapy.precession import ln_get_equ_prec
from nova.novapy.precession import ln_get_equ_prec2
from nova.novapy.proper_motion import ln_get_equ_pm
from nova.novapy.api.constants import JD2000
from nova.novapy.api.constants import JD2050
from nova.novapy.api.constants import B1900
# for apparent position test
from nova.novapy.apparent_position import ln_get_apparent_posn
# for vsop87 test
from nova.novapy.solar_system.solar import ln_get_solar_equ_coords
from nova.novapy.solar_system.mercury import ln_get_mercury_helio_coords
from nova.novapy.solar_system.mercury import ln_get_mercury_equ_coords
from nova.novapy.solar_system.mercury import ln_get_mercury_earth_dist
from nova.novapy.solar_system.mercury import ln_get_mercury_solar_dist
from nova.novapy.solar_system.mercury import ln_get_mercury_phase
from nova.novapy.solar_system.mercury import ln_get_mercury_disk
from nova.novapy.solar_system.mercury import ln_get_mercury_magnitude
from nova.novapy.solar_system.mercury import ln_get_mercury_sdiam
from nova.novapy.solar_system.mercury import ln_get_mercury_rst
from nova.novapy.solar_system.mercury import ln_get_mercury_rect_helio
from nova.novapy.solar_system.venus import ln_get_venus_helio_coords
from nova.novapy.solar_system.venus import ln_get_venus_equ_coords
from nova.novapy.solar_system.venus import ln_get_venus_earth_dist
from nova.novapy.solar_system.venus import ln_get_venus_solar_dist
from nova.novapy.solar_system.venus import ln_get_venus_phase
from nova.novapy.solar_system.venus import ln_get_venus_disk
from nova.novapy.solar_system.venus import ln_get_venus_magnitude
from nova.novapy.solar_system.venus import ln_get_venus_sdiam
from nova.novapy.solar_system.mars import ln_get_mars_helio_coords
from nova.novapy.solar_system.mars import ln_get_mars_equ_coords
from nova.novapy.solar_system.mars import ln_get_mars_earth_dist
from nova.novapy.solar_system.mars import ln_get_mars_solar_dist
from nova.novapy.solar_system.mars import ln_get_mars_phase
from nova.novapy.solar_system.mars import ln_get_mars_disk
from nova.novapy.solar_system.mars import ln_get_mars_magnitude
from nova.novapy.solar_system.mars import ln_get_mars_sdiam

from nova.novapy.solar_system.lunar import load_data
from nova.novapy.solar_system.lunar import ln_get_lunar_geo_posn

from nova.novapy.solar_system.jupiter import ln_get_jupiter_helio_coords
from nova.novapy.solar_system.jupiter import ln_get_jupiter_equ_coords
from nova.novapy.solar_system.jupiter import ln_get_jupiter_earth_dist
from nova.novapy.solar_system.jupiter import ln_get_jupiter_solar_dist
from nova.novapy.solar_system.jupiter import ln_get_jupiter_phase
from nova.novapy.solar_system.jupiter import ln_get_jupiter_disk
from nova.novapy.solar_system.jupiter import ln_get_jupiter_magnitude
from nova.novapy.solar_system.jupiter import ln_get_jupiter_equ_sdiam

from nova.novapy.api.ln_lnlat_posn import LnLnlatPosn
from nova.novapy.solar_system.solar import ln_get_solar_rst
from nova.novapy.api.ln_rst_time import LnRstTime
from nova.novapy.julian_day import ln_get_zonedate_from_sys

from nova.novapy.solar_system.saturn import ln_get_saturn_equ_coords
from nova.novapy.solar_system.saturn import ln_get_saturn_helio_coords
from nova.novapy.solar_system.saturn import ln_get_saturn_earth_dist
from nova.novapy.solar_system.saturn import ln_get_saturn_solar_dist
from nova.novapy.solar_system.saturn import ln_get_saturn_magnitude
from nova.novapy.solar_system.saturn import ln_get_saturn_disk
from nova.novapy.solar_system.saturn import ln_get_saturn_phase
from nova.novapy.solar_system.saturn import ln_get_saturn_rst
from nova.novapy.solar_system.saturn import ln_get_saturn_equ_sdiam
from nova.novapy.solar_system.saturn import ln_get_saturn_pol_sdiam
from nova.novapy.solar_system.saturn import ln_get_saturn_rect_helio

from nova.novapy.solar_system.uranus import ln_get_uranus_equ_coords
from nova.novapy.solar_system.uranus import ln_get_uranus_helio_coords
from nova.novapy.solar_system.uranus import ln_get_uranus_earth_dist
from nova.novapy.solar_system.uranus import ln_get_uranus_solar_dist
from nova.novapy.solar_system.uranus import ln_get_uranus_magnitude
from nova.novapy.solar_system.uranus import ln_get_uranus_disk
from nova.novapy.solar_system.uranus import ln_get_uranus_phase
from nova.novapy.solar_system.uranus import ln_get_uranus_rst
from nova.novapy.solar_system.uranus import ln_get_uranus_sdiam
from nova.novapy.solar_system.uranus import ln_get_uranus_rect_helio

from nova.novapy.solar_system.earth import ln_get_earth_solar_dist
from nova.novapy.solar_system.earth import ln_get_earth_helio_coords
from nova.novapy.utility import ln_equ_to_hequ

from nova.novapy.solar_system.lunar import ln_get_lunar_ecl_coords
from nova.novapy.solar_system.lunar import ln_get_lunar_earth_dist
from nova.novapy.solar_system.lunar import ln_get_lunar_equ_coords_prec
from nova.novapy.solar_system.lunar import ln_get_lunar_equ_coords
from nova.novapy.solar_system.lunar import ln_get_lunar_phase
from nova.novapy.solar_system.lunar import ln_get_lunar_bright_limb
from nova.novapy.solar_system.lunar import ln_get_lunar_disk
from nova.novapy.solar_system.lunar import ln_get_lunar_long_asc_node
from nova.novapy.solar_system.lunar import ln_get_lunar_long_perigee
from nova.novapy.solar_system.lunar import ln_get_lunar_rst
from nova.novapy.solar_system.lunar import ln_get_lunar_sdiam

from time import sleep


class TestRunner:
    test_number = 0

    def __init__(self):
        pass

    def test_result(self, test, calc, expect, tolerance):
        self.test_number += 1
        diff = compare_results(calc, expect, tolerance)
        if diff is not 0:
            print('[Failed] \t Expected {0} but calculated {1}  {2} error.'.format(expect, calc, diff))
            return -1
        else:
            print('[Test : Passed]{0}> Expected and calculated {1}.'.format(test, calc))
            return 0

    def julian_test(self):
        date = LnDate()
        pdate = LnDate()
        zonedate = LnZoneDate()
        failed = 0
        # Get julian day for 04 / 10 / 1957 19: 00: 00
        date.years = 1957
        date.months = 10
        date.days = 4
        date.hours = 19
        date.minutes = 0
        date.seconds = 0
        jd = float()
        jd2 = float()
        jd = ln_get_julian_day(date)
        failed += self.test_result('(Julian Day) JD for 4/10/1957 19:00:00', jd, 2436116.29166667, 0.00001)

        #  Get julian day for 30/06/1954 00:00:00
        date.years = 1954
        date.months = 6
        date.days = 30
        date.hours = 0
        jd = ln_get_julian_day(date)
        failed += self.test_result('(Julian Day) JD for 30/06/1954 00:00:00', jd, 2434923.5, 0.1)

        wday = ln_get_day_of_week(date)
        failed += self.test_result('(Julian Day) Weekday No', wday, 3, 0.1)

        ln_date_to_zonedate(date, zonedate, -21600)
        ln_zonedate_to_date(zonedate, date)

        jd = ln_get_julian_day(date)
        string = '(Julian Day) ln_date_to_zonedate and ln_zonedate_to_date check - JD for 30/06/1954 00:00:00'
        failed += self.test_result(string, jd, 2434923.5, 0.1)

        ln_get_date_from_sys(date)
        jd = ln_get_julian_from_sys()

        print('{0}/{1}/{2}   {3}:{4}:{5}:{6}'.format(date.months, date.days, date.years, date.hours, date.minutes,
                                                     date.seconds, date.millis))
        sleep(1)
        jd2 = ln_get_julian_from_sys()

        print('{0}/{1}/{2}   {3}:{4}:{5}:{6}'.format(date.months, date.days, date.years, date.hours, date.minutes,
                                                     date.seconds, date.millis))

        string = '(Julian Day)Diferrence between two successive ln_get_julian_from_sys() calls (it shall never be zero)'

        self.test_result(string, jd2 - jd, 1 ** -2 / 86400.0, .99 ** -1)

    def dynamical_test(self):
        date = LnDate()

        date.years = 2000
        date.months = 1
        date.days = 1
        date.hours = 0
        date.minutes = 0
        date.seconds = 0.0

        JD = ln_get_julian_day(date)
        TD = ln_get_jde(JD)
        failed = 0
        failed += self.test_result('(Dynamical Time) TD for 01/01/2000 00:00:00', TD, 2451544.50073877, 0.000001)

    def heliocentric_test(self):
        obj = LnEquPosn()
        date = LnDate()
        failed = 0

        obj.ra = 0.0
        obj.dec = 60.0

        date.years = 2000
        date.months = 1
        date.days = 1
        date.hours = 0
        date.minutes = 0
        date.seconds = 0.0

        JD = ln_get_julian_day(date)

        diff = ln_get_heliocentric_time_diff(JD, obj)
        failed += self.test_result('(Heliocentric time) TD for 01/01, obj on 18h +50', diff, -16.0 * 0.0001, 0.0001)

        date.months = 8
        date.days = 8

        JD = ln_get_julian_day(date)

        diff = ln_get_heliocentric_time_diff(JD, obj)

        failed += self.test_result('(Heliocentric time) TD for 08/08, obj on 18h +50', diff, 12.0 * 0.0001, 0.0001)

    def nutation_test(self):
        nutation = LnNutation()
        failed = 0

        jd = 2446895.5

        ln_get_nutation(jd, nutation)
        string = '(Nutation) longitude (deg) for JD 2446895.5'
        failed += self.test_result(string, nutation.longitude, -0.00105222, 0.00000001)
        string = '(Nutation) obliquity (deg) for JD 2446895.5'
        failed += self.test_result(string, nutation.obliquity, 0.00262293, 0.00000001)
        string = '(Nutation) ecliptic (deg) for JD 2446895.5'
        failed += self.test_result(string, nutation.ecliptic, 23.44094649, 0.00000001)

    def transform_test(self):
        h_obj = LnhEquPosn()
        h_pollux = LnhEquPosn()

        h_observer = LnhLnlatPosn()
        hecl = LnhLnlatPosn()

        observer = LnLnlatPosn()
        ecl = LnLnlatPosn()

        gal = LnGalPosn()

        obj = LnEquPosn()
        pollux = LnEquPosn()
        equ = LnEquPosn()

        hrz = LnHrzPosn()

        date = LnDate()

        failed = 0

        h_observer.lng.neg = 0
        h_observer.lng.degrees = 282
        h_observer.lng.minutes = 56
        h_observer.lng.seconds = 4.0
        h_observer.lat.neg = 0
        h_observer.lat.degrees = 38
        h_observer.lat.minutes = 55
        h_observer.lat.seconds = 17.0

        h_obj.ra.hours = 23
        h_obj.ra.minutes = 9
        h_obj.ra.seconds = 16.641
        h_obj.dec.neg = 1
        h_obj.dec.degrees = 6
        h_obj.dec.minutes = 43
        h_obj.dec.seconds = 11.61

        date.years = 1987
        date.months = 4
        date.days = 10
        date.hours = 19
        date.minutes = 21
        date.seconds = 0.0

        JD = ln_get_julian_day(date)
        ln_hequ_to_equ(h_obj, obj)
        ln_hlnlat_to_lnlat(h_observer, observer)

        ln_get_hrz_from_equ(obj, observer, JD, hrz)
        failed += self.test_result('(Transforms) Equ to Horiz ALT ', hrz.alt, 15.12426274, 0.00000001)
        failed += self.test_result('(Transforms) Equ to Horiz AZ ', hrz.az, 68.03429264, 0.00000001)

        obj.dec = 90.0

        ln_get_hrz_from_equ(obj, observer, JD, hrz)
        failed += self.test_result('(Transforms) Equ to Horiz ALT ', hrz.alt, 38.9213888888, 0.00000001)
        failed += self.test_result('(Transforms) Equ to Horiz AZ ', hrz.az, 180.0, 0.00000001)

        obj.dec = -90.0

        ln_get_hrz_from_equ(obj, observer, JD, hrz)
        failed += self.test_result('(Transforms) Equ to Horiz ALT ', hrz.alt, -38.9213888888, 0.00000001)
        failed += self.test_result('(Transforms) Equ to Horiz AZ ', hrz.az, 0.0, 0.00000001)

        observer.lat *= -1.0

        ln_get_hrz_from_equ(obj, observer, JD, hrz)
        failed += self.test_result('(Transforms) Equ to Horiz ALT ', hrz.alt, 38.9213888888, 0.00000001)
        failed += self.test_result('(Transforms) Equ to Horiz AZ ', hrz.az, 0.0, 0.00000001)

        obj.dec = 90.0

        ln_get_hrz_from_equ(obj, observer, JD, hrz)
        failed += self.test_result('(Transforms) Equ to Horiz ALT ', hrz.alt, -38.9213888888, 0.00000001)
        failed += self.test_result('(Transforms) Equ to Horiz AZ ', hrz.az, 180.0, 0.00000001)

        h_pollux.ra.hours = 7
        h_pollux.ra.minutes = 45
        h_pollux.ra.seconds = 18.946
        h_pollux.dec.neg = 0
        h_pollux.dec.degrees = 28
        h_pollux.dec.minutes = 1
        h_pollux.dec.seconds = 34.26

        ln_hequ_to_equ(h_pollux, pollux)
        ln_get_ecl_from_equ(pollux, JD, ecl)

        ln_lnlat_to_hlnlat(ecl, hecl)
        failed += self.test_result('(Transforms) Equ to Ecl longitude ', ecl.lng, 113.21555278, 0.00000001)
        failed += self.test_result('(Transforms) Equ to Ecl latitude', ecl.lat, 6.68264899, 0.00000001)

        ln_get_equ_from_ecl(ecl, JD, equ)
        failed += self.test_result('(Transforms) Ecl to Equ RA ', equ.ra, 116.32894167, 0.00000001)
        failed += self.test_result('(Transforms) Ecl to Equ DEC', equ.dec, 28.02618333, 0.00000001)

        gal.l = 0.0
        gal.b = 90.0

        ln_get_equ_from_gal(gal, equ)
        failed += self.test_result('(Transforms) Gal to Equ RA', equ.ra, 192.25, 0.00000001)
        failed += self.test_result('(Transforms) Gal to Equ DEC', equ.dec, 27.4, 0.00000001)

        ln_get_gal_from_equ(equ, gal)
        failed += self.test_result('(Transforms) Equ to Gal b', gal.b, 90, 0.00000001)

    def sidereal_test(self):
        date = LnDate()
        failed = 0

        # 10/04/1987 19:21:00
        date.years = 1987
        date.months = 4
        date.days = 10
        date.hours = 19
        date.minutes = 21
        date.seconds = 0.0

        JD = ln_get_julian_day(date)
        sd = ln_get_mean_sidereal_time(JD)

        failed += self.test_result('(Sidereal) mean hours on 10/04/1987 19:21:00 ', sd, 8.58252488, 0.000001)
        sd = ln_get_apparent_sidereal_time(JD)
        failed += self.test_result('(Sidereal) apparent hours on 10/04/1987 19:21:00 ', sd, 8.58245327, 0.000001)

    def solar_coord_test(self):
        pos = LnHelioPosn()
        equ_pos = LnEquPosn()
        observer = LnLnlatPosn()
        rst = LnRstTime()
        rise_time, transit_time, set_time = LnZoneDate(), LnZoneDate(), LnZoneDate()
        date = LnDate()
        zonedate = LnZoneDate()
        # 39.7392° N, 104.9903° W Denver
        observer.lat = 39.7392
        observer.lng = -104.9903

        jd = ln_get_julian_from_sys()
        ln_get_date(jd, date)
        print('Solar Test for JD date {0} [{1}]'.format(jd, date.get_string()))
        print('--------------------------------------------------------------')
        ln_get_solar_geom_coords(jd, pos)
        print('Solar Geometric Coordinates:')
        print('\tlongitude    (deg): ', pos.l)
        print('\tlatitude     (deg): ', pos.b)
        print('\tradius vector (AU): ', pos.r)
        ln_get_solar_equ_coords(jd, equ_pos)
        print('Solar Geometric Coordinates:')
        print('\t RA: ', equ_pos.ra)
        print('\tDEC: ', equ_pos.dec)
        print('Rise, Transit, and Set:')

        if ln_get_solar_rst(jd, observer, rst) == 1:
            print('The Sun is circumpolar.')
        else:
            ln_get_date(rst.rise, rise_time)
            ln_get_date(rst.transit, transit_time)
            ln_get_date(rst.set, set_time)
            ln_date_to_zonedate(rise_time, zonedate, -21600)
            print('Rise: ', rise_time.get_string())
            print(zonedate.get_string())
            print('Transit: ', transit_time.get_string())
            print('Set: ', set_time.get_string())

        # ln_get_solar_geom_coords(2448908.5, pos)

    def aberration_test(self):
        date = LnDate()
        h_obj = LnhEquPosn()
        obj = LnEquPosn()
        pos = LnEquPosn()
        failed = 0

        h_obj.ra.hours = 2
        h_obj.ra.minutes = 44
        h_obj.ra.seconds = 12.9747
        h_obj.dec.neg = 0
        h_obj.dec.degrees = 49
        h_obj.dec.minutes = 13
        h_obj.dec.seconds = 39.896

        date.years = 2028
        date.months = 11
        date.days = 13
        date.hours = 4
        date.minutes = 31
        date.seconds = 0

        JD = ln_get_julian_day(date)

        ln_hequ_to_equ(h_obj, obj)
        ln_get_equ_aber(obj, JD, pos)
        failed += self.test_result('(Aberration) RA  ', pos.ra, 41.06238352, 0.00000001)
        failed += self.test_result('(Aberration) DEC  ', pos.dec, 49.22962359, 0.00000001)
        # end aberration_test

    def precession_test(self):
        obj = LnEquPosn()
        pos = LnEquPosn()
        pos2 = LnEquPosn()
        pm = LnEquPosn()
        h_obj = LnhEquPosn()
        grb_date = LnDate()
        failed = 0

        h_obj.ra.hours = 2
        h_obj.ra.minutes = 44
        h_obj.ra.seconds = 11.986
        h_obj.dec.neg = 0
        h_obj.dec.degrees = 49
        h_obj.dec.minutes = 13
        h_obj.dec.seconds = 42.48

        JD = 2462088.69
        ln_hequ_to_equ(h_obj, obj)

        pm.ra = 0.03425 * (15.0 / 3600.0)
        pm.dec = -0.0895 / 3600.0

        ln_get_equ_pm(obj, pm, JD, obj)

        failed += self.test_result('(Proper motion) RA on JD 2462088.69  ', obj.ra, 41.054063, 0.00001)
        failed += self.test_result('(Proper motion) DEC on JD 2462088.69  ', obj.dec, 49.227750, 0.00001)

        ln_get_equ_prec(obj, JD, pos)
        failed += self.test_result('(Precession) RA on JD 2462088.69  ', pos.ra, 41.547214, 0.00003)
        failed += self.test_result('(Precession) DEC on JD 2462088.69  ', pos.dec, 49.348483, 0.00001)

        ln_get_equ_prec2(obj, JD2000, JD, pos)

        failed += self.test_result('(Precession 2) RA on JD 2462088.69  ', pos.ra, 41.547214, 0.00003)
        failed += self.test_result('(Precession 2) DEC on JD 2462088.69  ', pos.dec, 49.348483, 0.00001)

        ln_get_equ_prec2(pos, JD, JD2000, pos2)

        failed += self.test_result('(Precession 2) RA on JD 2451545.0  ', pos2.ra, obj.ra, 0.00001)
        failed += self.test_result('(Precession 2) DEC on JD 2451545.0  ', pos2.dec, obj.dec, 0.00001)

        pos.ra = 271.2473
        pos.dec = -32.0227

        grb_date.years = 2005
        grb_date.months = 9
        grb_date.days = 22
        grb_date.hours = 13
        grb_date.minutes = 43
        grb_date.seconds = 18.0

        JD = ln_get_julian_day(grb_date)

        ln_get_equ_prec2(pos, JD, JD2000, pos2)

        failed += self.test_result('(Precession 2) RA on JD 2451545.0  ', pos2.ra, 271.1541, 0.0002)
        failed += self.test_result('(Precession 2) DEC on JD 2451545.0  ', pos2.dec, -32.0235, 0.0002)

        h_obj.ra.hours = 2
        h_obj.ra.minutes = 31
        h_obj.ra.seconds = 48.704
        h_obj.dec.neg = 0
        h_obj.dec.degrees = 89
        h_obj.dec.minutes = 15
        h_obj.dec.seconds = 50.72

        ln_hequ_to_equ(h_obj, obj)

        pm.ra = 0.19877 * (15.0 / 3600.0)
        pm.dec = -0.0152 / 3600.0

        ln_get_equ_pm(obj, pm, B1900, pos)

        ln_get_equ_prec2(pos, JD2000, B1900, pos2)

        failed += self.test_result('(Precision 2) RA on B1900  ', pos2.ra, 20.6412499980, 0.002)
        failed += self.test_result('(Precision 2) DEC on B1900  ', pos2.dec, 88.7739388888, 0.0001)

        ln_get_equ_pm(obj, pm, JD2050, pos)

        ln_get_equ_prec2(pos, JD2000, JD2050, pos2)

        failed += self.test_result('(Precision 2) RA on J2050  ', pos2.ra, 57.0684583320, 0.003)
        failed += self.test_result('(Precision 2) DEC on J2050  ', pos2.dec, 89.4542722222, 0.0001)

        # end precession_test

    def apparent_position_test(self):
        h_obj = LnhEquPosn()
        h_pm = LnhEquPosn()
        obj = LnEquPosn()
        pm = LnEquPosn()
        pos = LnEquPosn()
        failed = 0

        h_obj.ra.hours = 2
        h_obj.ra.minutes = 44
        h_obj.ra.seconds = 12.9747
        h_obj.dec.neg = 0
        h_obj.dec.degrees = 49
        h_obj.dec.minutes = 13
        h_obj.dec.seconds = 39.896

        h_pm.ra.hours = 0
        h_pm.ra.minutes = 0
        h_pm.ra.seconds = 0.03425
        h_pm.dec.neg = 1
        h_pm.dec.degrees = 0
        h_pm.dec.minutes = 0
        h_pm.dec.seconds = 0.0895

        JD = 2462088.69
        ln_hequ_to_equ(h_obj, obj)
        ln_hequ_to_equ(h_pm, pm)
        ln_get_apparent_posn(obj, pm, JD, pos)

        failed += self.test_result('(Apparent Position) RA on JD 2462088.69  ', pos.ra, 41.55966517, 0.00000001)
        failed += self.test_result('(Apparent Position) DEC on JD 2462088.69  ', pos.dec, 49.34962340, 0.00000001)
        # end apparent_position_test

    def vsop87_test(self):
        pos = LnHelioPosn()
        hequ = LnhEquPosn()
        equ = LnEquPosn()
        date = LnDate()
        JD = 2448976.5
        failed = 0
        observer = LnLnlatPosn()
        observer.lat = 39.742043
        observer.lng = -104.991531
        au = 0

        ln_get_solar_equ_coords(JD, equ)

        failed += self.test_result('(Solar Position) RA on JD 2448976.5  ', equ.ra, 268.32141013, 0.00000001)
        failed += self.test_result('(Solar Position) DEC on JD 2448976.5  \n', equ.dec, -23.43013835, 0.00000001)
        print('-------------------------------------------------')
        ln_get_mercury_helio_coords(JD, pos)
        ln_get_mercury_equ_coords(JD, equ)
        ln_equ_to_hequ(equ, hequ)
        print('| Mercury | RA:  {0}:{1}:{2}'.format(hequ.ra.hours, hequ.ra.minutes, hequ.ra.seconds))
        print('|---------| DEC: {0}:{1}:{2}'.format(hequ.dec.degrees, hequ.dec.minutes, hequ.dec.seconds))
        print('|L {0} B {1} R {2}'.format(pos.l, pos.b, pos.r))
        au = ln_get_mercury_earth_dist(JD)
        print('|\t\t Earth dist (AU) {0}'.format(au))
        au = ln_get_mercury_solar_dist(JD)
        print('|\t\t Sun dist (AU) {0}'.format(au))
        au = ln_get_mercury_disk(JD)
        print('|\t\t illuminated disk {0}'.format(au))
        au = ln_get_mercury_magnitude(JD)
        print('|\t\t magnitude {0}'.format(au))
        au = ln_get_mercury_phase(JD)
        print('|\t\t phase {0}'.format(au))
        au = ln_get_mercury_sdiam(JD)
        print('|\t\t sdiam {0}'.format(au))

        print('-------------------------------------------------')
        ln_get_venus_helio_coords(JD, pos)
        ln_get_venus_equ_coords(JD, equ)
        ln_equ_to_hequ(equ, hequ)
        au = ln_get_venus_earth_dist(JD)
        print('| Venus   | RA:  {0}:{1}:{2}'.format(hequ.ra.hours, hequ.ra.minutes, hequ.ra.seconds))
        print('|---------| DEC: {0}:{1}:{2}'.format(hequ.dec.degrees, hequ.dec.minutes, hequ.dec.seconds))

        print('|L {0}\t\t Earth dist (AU) {1}'.format(pos.l, au))
        au = ln_get_venus_solar_dist(JD)
        print('|B {0}\t\t Sun dist (AU) {1}'.format(pos.b, au))
        au = ln_get_venus_disk(JD)
        print('|R {0}\t\t illuminated disk {1}'.format(pos.r, au))
        au = ln_get_venus_magnitude(JD)
        print('|\t\t\t\t magnitude ', au)
        au = ln_get_venus_phase(JD)
        print('|\t\t\t\t phase ', au)
        au = ln_get_venus_sdiam(JD)
        print('|\t\t\t\t sdiam ', au)

        print('-------------------------------------------------')
        ln_get_earth_helio_coords(JD, pos)
        print('Earth L {0} B {1} R {2}'.format(pos.l, pos.b, pos.r))
        au = ln_get_earth_solar_dist(JD)

        print('earth -> Sun dist (AU) {0}'.format(au))
        print('-------------------------------------------------')
        ln_get_mars_helio_coords(JD, pos)
        ln_get_mars_equ_coords(JD, equ)
        ln_equ_to_hequ(equ, hequ)
        au = ln_get_mars_earth_dist(JD)
        print('| Mars    | RA:  {0}:{1}:{2}'.format(hequ.ra.hours, hequ.ra.minutes, hequ.ra.seconds))
        print('|---------| DEC: {0}:{1}:{2}'.format(hequ.dec.degrees, hequ.dec.minutes, hequ.dec.seconds))

        print('|L {0}\t\t Earth dist (AU) {1}'.format(pos.l, au))
        au = ln_get_mars_solar_dist(JD)
        print('|B {0}\t\t Sun dist (AU) {1}'.format(pos.b, au))
        au = ln_get_mars_disk(JD)
        print('|R {0}\t\t illuminated disk {1}'.format(pos.r, au))
        au = ln_get_mars_magnitude(JD)
        print('|\t\t\t\t magnitude ', au)
        au = ln_get_mars_phase(JD)
        print('|\t\t\t\t phase ', au)
        au = ln_get_mars_sdiam(JD)
        print('|\t\t\t\t sdiam ', au)
        print('-------------------------------------------------')
        print('-------------------------------------------------')
        ln_get_jupiter_helio_coords(JD, pos)
        ln_get_jupiter_equ_coords(JD, equ)
        ln_equ_to_hequ(equ, hequ)
        au = ln_get_jupiter_earth_dist(JD)
        print('| Jupiter | RA:  {0}:{1}:{2}'.format(hequ.ra.hours, hequ.ra.minutes, hequ.ra.seconds))
        print('|---------| DEC: {0}:{1}:{2}'.format(hequ.dec.degrees, hequ.dec.minutes, hequ.dec.seconds))

        print('|L {0}\t\t Earth dist (AU) {1}'.format(pos.l, au))
        au = ln_get_jupiter_solar_dist(JD)
        print('|B {0}\t\t Sun dist (AU) {1}'.format(pos.b, au))
        au = ln_get_jupiter_disk(JD)
        print('|R {0}\t\t illuminated disk {1}'.format(pos.r, au))
        au = ln_get_jupiter_magnitude(JD)
        print('|\t\t\t\t magnitude ', au)
        au = ln_get_jupiter_phase(JD)
        print('|\t\t\t\t phase ', au)
        au = ln_get_jupiter_equ_sdiam(JD)
        print('|\t\t\t\t sdiam ', au)
        print('-------------------------------------------------')
        ln_get_saturn_helio_coords(JD, pos)
        ln_get_saturn_equ_coords(JD, equ)
        ln_equ_to_hequ(equ, hequ)
        au = ln_get_saturn_earth_dist(JD)
        print('| Saturn  | RA:  {0}:{1}:{2}'.format(hequ.ra.hours, hequ.ra.minutes, hequ.ra.seconds))
        print('|---------| DEC: {0}:{1}:{2}'.format(hequ.dec.degrees, hequ.dec.minutes, hequ.dec.seconds))

        print('|L {0}\t\t Earth dist (AU) {1}'.format(pos.l, au))
        au = ln_get_saturn_solar_dist(JD)
        print('|B {0}\t\t Sun dist (AU) {1}'.format(pos.b, au))
        au = ln_get_saturn_disk(JD)
        print('|R {0}\t\t illuminated disk {1}'.format(pos.r, au))
        au = ln_get_saturn_magnitude(JD)
        print('|\t\t\t\t magnitude ', au)
        au = ln_get_saturn_phase(JD)
        print('|\t\t\t\t phase ', au)
        au = ln_get_saturn_equ_sdiam(JD)
        print('|\t\t\t\t sdiam ', au)
        print('-------------------------------------------------')

        jd = ln_get_date_from_sys(date)
        print('[test] jd = ', jd)
        jd = ln_get_julian_day(date)
        print('[test] jd = ', jd)
        date.print_debug()
        zd = LnZoneDate()
        ln_get_zonedate_from_sys(zd)
        print('{0}/{1}/{2}   {3}:{4}:{5}   {6}'.format(zd.months, zd.days, zd.years, zd.hours, zd.minutes,
                                                       zd.seconds, zd.gmtoff))
        # date.print_debug()
        ln_zonedate_to_date(zd, date)
        # date.print_debug()
        ln_get_date_from_sys(date)
        jd = ln_get_julian_day(date)
        print('[test] jd = ', jd)
        date.print_debug()

        # val = (dist2 - dist1) / (jd2 - jd)
        # print('\t Earths velocity away from the sun: ', val)

    def lunar_test(self):
        date = LnDate()
        observer = LnLnlatPosn()
        observer.lat = 39.742043
        observer.lng = -104.991531
        ln_get_date_from_sys(date)
        jd = 2448724.5
        #  JD = ln_get_julian_from_sys()
        print(date.get_string())
        moon = LnRectPosn()
        equ = LnEquPosn()
        ecl = LnLnlatPosn()

        ln_get_lunar_geo_posn(jd, moon, 0)
        print('{0} {1} {2}'.format(moon.x, moon.y, moon.z))
        ln_get_lunar_ecl_coords(jd, ecl, 0)
        print('long = {0}\tlat = {1}'.format(ecl.lng, ecl.lat))
        ln_get_lunar_equ_coords(jd, equ)

        print('ra = {0}\tdec = {1}'.format(equ.ra, equ.dec))

        print('distance = ', ln_get_lunar_earth_dist(jd))

    def au_to_mile(self, au):
        # AU to kilometer
        convert = 149597870700. / 1000.
        # to inch
        return convert * 39370.1

    def run_tests(self):
        '''
                self.julian_test()
                self.dynamical_test()
                self.heliocentric_test()
                self.nutation_test()
                self.transform_test()
                self.sidereal_test()
                self.solar_coord_test()
                self.aberration_test()
                self.precession_test()
                self.apparent_position_test()
        '''
        self.vsop87_test()
        self.lunar_test()
        self.solar_coord_test()


def compare_results(calc, expect, tolerance):
    if tolerance * -1.0 > calc - expect > tolerance:
        return calc - expect
    else:
        return 0


from nova.novapy.solar_system.lunar import elp36_sol_pert


tester = TestRunner()
tester.run_tests()
