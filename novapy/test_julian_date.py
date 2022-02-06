from unittest import TestCase
from unittest import main
from novapy.api.ln_date import LnDate
from novapy.api.ln_zone_date import LnZoneDate
from novapy.julian_day import ln_get_date
from novapy.julian_day import ln_get_julian_day
from novapy.julian_day import ln_get_day_of_week
from novapy.julian_day import ln_date_to_zonedate
from novapy.julian_day import ln_zonedate_to_date
from novapy.julian_day import ln_get_date_from_sys
from novapy.julian_day import ln_get_julian_from_sys
from novapy.julian_day import ln_get_zonedate_from_sys
from novapy.julian_day import ln_get_julian_from_mpc
from novapy.util.time_zones import TimeZoneHandler
from novapy.julian_day import ln_get_mpc_from_date
def test_result(test, calc, expect, tolerance):

    diff = compare_results(calc, expect, tolerance)
    if diff is not 0:
        print('[Failed] \t Expected {0} but calculated {1}  {2} error.'.format(expect, calc, diff))
        return -1
    else:
        print('[Test : Passed]{0}> Expected and calculated {1}:\t{2}.'.format(test, expect, calc))
        return 0


def compare_results(calc, expect, tolerance):
    if tolerance * -1.0 > calc - expect > tolerance:
        return calc - expect
    else:
        return 0


class JulianTestCase(TestCase):
    def test_date(self):
        date = LnDate()
        pdate = LnDate()
        zonedate = LnZoneDate()
        tzh = TimeZoneHandler.getMaster()
        failed = 0
        # Get julian day for 04 / 10 / 1957 19: 00: 00
        date.years = 1957
        date.months = 10
        date.days = 4
        date.hours = 19
        date.minutes = 0
        date.seconds = 1
        jd = float()
        jd2 = float()
        jd = ln_get_julian_day(date)
        print(2436116.29166667)
        #failed += test_result('(Julian Day) JD for 4/10/1957 19:00:00', jd, 2436116.29166667, 0.00001)
        self.assertEqual(test_result('JD for {0}'.format(date.get_string()), jd, 2436116.29166667, 0.000001), 0)
        ln_get_date(jd, pdate)
        print(pdate.get_string())
        ln_get_zonedate_from_sys(zonedate)
        print('Now: ', zonedate.get_string())
        jd = ln_get_julian_from_sys()
        ln_zonedate_to_date(zonedate,date)
        print('Date:\t', date.get_string())
        print('Zone Date: ', zonedate.get_string())
        print('Testing Julian Date From MPC date [K183N525]')
        jd = ln_get_julian_from_mpc('K1811525')
        ln_get_date(jd, date)
        print(date.print_debug())
        mpc_date = ln_get_mpc_from_date(date)
        print(mpc_date)
        jd = ln_get_julian_from_mpc(mpc_date)
        ln_get_date(jd, date)
        print(date.print_debug())
        jd = ln_get_julian_from_sys()
        observer = LnLnlatPosn()
        rst = LnRstTime()
        hms = LnHms()
        dms = LnDms()
        equ_obj = LnEquPosn()

        # Arcturus
        hms.hours = 14
        hms.minutes = 15
        hms.seconds = 39.67
        dms.neg = 0
        dms.degrees = 19
        dms.minutes = 10
        dms.seconds = 56.7
        equ_obj.ra = ln_hms_to_deg(hms)
        equ_obj.dec = ln_dms_to_deg(dms)
        ret = ln_get_object_rst(jd, observer, equ_obj, rst)
        ln_get_date(rst.rise, date)
        ln_date_to_zonedate(date, zonedate, -21600)
        print(date.get_string())
        print(zonedate.get_string())
        ln_get_date(rst.transit, date)
        ln_date_to_zonedate(date, zonedate, -21600)
        print(date.get_string())
        print(zonedate.get_string())
        ln_get_date(rst.set, date)
        ln_date_to_zonedate(date, zonedate, -21600)
        print(date.get_string())
        print(zonedate.get_string())
        print(rst.rise)
from novapy.julian_day import ln_date_to_zonedate
from novapy.riseset import ln_get_object_rst
from novapy.utility import ln_hms_to_deg
from novapy.utility import ln_dms_to_deg
from novapy.api.ln_lnlat_posn import LnLnlatPosn
from novapy.api.ln_rst_time import LnRstTime
from novapy.api.ln_hms import LnHms
from novapy.api.ln_dms import LnDms
from novapy.api.ln_equ_posn import LnEquPosn
main()