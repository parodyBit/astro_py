from novapy.api.ln_date import LnDate
from time import time
from datetime import datetime
from math import modf


MJD_0 = 2400000.5

def fpart(x):
    """Return fractional part of given number."""
    return modf(x)[0]


def ipart(x):
    """Return integer part of given number."""
    return modf(x)[1]

def ln_get_julian_day(date):
    local_date = LnDate()
    local_date.copy(date)

    year = int(local_date.years)
    month = int(local_date.months)
    day = int(local_date.days)
    hours = int(local_date.hours)
    minutes = int(local_date.minutes)
    seconds = float(local_date.seconds)

    a = ipart((month - 14) / 12.0)
    jd = ipart((1461.0 * (year + 4800.0 + a)) / 4.0)
    jd += ipart((367.0 * (month - 2.0 - 12.0 * a)) / 12.0)
    x = ipart((year + 4900.0 + a) / 100.0)
    jd -= ipart((3.0 * x) / 4.0)
    jd += day - 2432075.5  # was 32075; add 2400000.5
    jd += fpart(hours / 24.0)  #
    jd += fpart(minutes / 1440.0)
    jd += fpart(seconds / 86400.0)
    jd -= 0.5
    # print(60 * 60 * 24)
    '''
    y = ((x / 99.0) * 2) - 1
    day = 1
    24 hr = 1
    
    '''


    #jd -= 0.5  # 0 hours; above JD is for midday, switch to midnight.



    return jd + MJD_0


def ln_get_day_of_week(date):
    jd = ln_get_julian_day(date)
    jd += 1.5
    day = int(jd % 7)
    return day




def ln_get_date(jd, date):
    jd_f = fpart(jd)
    jd_i = ipart(jd)

    f = jd_f
    # set JD to noon of current date. Fractional part is the
    # fraction from midnight of the current date
    # if -0.5 >= f <= 0.5:
        # f += 0.5
    if f >= 0.5:
        jd_i += 1
        f -= 0.5
    elif f <= -0.5:
        jd_i -= 1
        f += 1.5
    l = jd_i + 68569
    n = ipart((4 * l) / 146097.0)
    l -= ipart(((146097 * n) + 3) / 4.0)
    i = ipart((4000 * (l + 1)) / 1461001)
    l -= ipart((1461 * i) / 4.0) - 31
    j = ipart((80 * l) / 2447.0)
    date.days = (l - ipart((2447 * j) / 80.0))
    l = ipart(j / 11.0)
    date.months = j + 2 - (12 * l)
    date.years = 100 * (n - 49) + i + l
    f += 0.5  # shift from noon to midnight for new day
    date.hours = int(f * 24)
    f -= date.hours / 24.
    date.minutes = int(f * 1440)
    f -= date.minutes / 1440.
    date.seconds = round(f * 86400)

from time import daylight
from time import tzname
from time import timezone
from novapy.util.time_zones import TimeZoneHandler
def ln_get_zonedate_from_sys(zone_date):
    now = int(round(time() * 1000))
    time_stamp = datetime.fromtimestamp(now / 1000.0)
    ts = (now * 1e-3)
    tzh = TimeZoneHandler.getMaster()
    # print(tzh.time_zones[tzname[0]].utc)
    print(tzname[0])
    utc_offset = (datetime.fromtimestamp(ts) - datetime.utcfromtimestamp(ts)).total_seconds()
    # zone_date.local_time = datetime.utcfromtimestamp(ts) + utc_offset
    zone_date.seconds = float(time_stamp.second)
    zone_date.minutes = int(time_stamp.minute)
    zone_date.hours = int(time_stamp.hour)
    zone_date.days = int(time_stamp.day)
    zone_date.months = int(time_stamp.month)
    zone_date.years = int(time_stamp.year)
    zone_date.gmtoff = utc_offset
    print(utc_offset / 3600)

def ln_get_date_from_sys(date):
    now = int(round(time() * 1000))
    time_stamp = datetime.fromtimestamp(now/1000.0)
    date.millis = float(time_stamp.microsecond/1000)
    date.seconds = float(time_stamp.second)
    date.minutes = int(time_stamp.minute)
    date.hours = int(time_stamp.hour)
    date.days = int(time_stamp.day)
    date.months = int(time_stamp.month)
    date.years = int(time_stamp.year)


def ln_get_date_from_utc_milliseconds(date, now):
    time_stamp = datetime.fromtimestamp(now/1000.0)
    date.seconds = float(time_stamp.second)
    date.hours = int(time_stamp.hour)
    date.days = int(time_stamp.day)
    date.months = int(time_stamp.month)
    date.years = int(time_stamp.year)

def ln_get_julian_from_timestamp(ts):
    return 2440587.5 + (ts / 86400.)

def ln_get_julian_from_sys():
    now = int(round(time()))
    ts = datetime.fromtimestamp(now)
    return 2440587.5 + (float(ts.timestamp()) / 86400.)
mpc_b31 = '0123456789ABCDEFGHIJKLMNOPQRZTUV'
def upack_mpc(char):
    return mpc_b31.find(char)
def pack_mpc(idx):
    return mpc_b31[idx]

def ln_get_date_from_mpc(date, mpc_date):



    idx = 0
    str_date = ''
    for p in mpc_date:
        str_date += str(upack_mpc(p))
        if idx < 5:
            if idx == 2:
                date.years = int(str_date)
                str_date = ''
            elif idx == 3:
                date.months = int(str_date)
                str_date = ''
            elif idx == 4:
                date.days = int(str_date)
                str_date = ''

        idx += 1
    fractional_day = '0.'
    fractional_day += str_date
    ftime = float(fractional_day)
    date.hours = int(ipart(100 * (ftime * (24/100))))
    ftime = fpart(100 * (ftime * (24/100)))
    date.minutes = int(ipart(100 * (ftime * (60/100))))
    ftime = fpart(100 * (ftime * (60/100)))
    date.seconds = float(ipart(100 * (ftime * (60/100))))




def ln_get_julian_from_mpc(mpc_date):
    date = LnDate()
    ln_get_date_from_mpc(date, mpc_date)
    jd = ln_get_julian_day(date)
    return jd

def ln_get_mpc_from_date(date):
    yr = str(date.years)
    m_yr = yr[0] + yr[1]
    t_yr = pack_mpc(int(m_yr))
    m_yr = yr[2] + yr[3]
    t_yr += m_yr
    t_yr += pack_mpc(int(date.months))
    t_yr += pack_mpc(int(date.days))
    rtime = 0
    rtime = (date.seconds/86400) + (date.minutes/1400) + (date.hours/24)
    t_yr += str(int(ipart(rtime*1000)))
    print(t_yr)
    return t_yr

def ln_get_local_date(jd, zonedate):
    date = LnDate()



def ln_date_to_zonedate(date, zonedate, gmt_offset):
    dat = LnDate()
    jd = ln_get_julian_day(date)
    if gmt_offset > 0:
        jd -= gmt_offset / 86400.0
    else:
        jd += gmt_offset / 86400.0
    ln_get_date(jd, dat)

    zonedate.years = dat.years
    zonedate.months = dat.months
    zonedate.days = dat.days

    zonedate.hours = dat.hours
    zonedate.minutes = dat.minutes
    zonedate.seconds = dat.seconds
    zonedate.gmtoff = gmt_offset


def ln_zonedate_to_date(zonedate, date):
    dat = LnDate()
    dat.years = zonedate.years
    dat.months = zonedate.months
    dat.days = zonedate.days
    dat.hours = zonedate.hours
    dat.minutes = zonedate.minutes
    dat.seconds = zonedate.seconds

    jd = ln_get_julian_day(dat)
    jd -= zonedate.gmtoff / 86400.
    ln_get_date(jd, date)

def convert_to_base(str_x, base):
    x = int(str_x)
    if x < 0:
        sign = -1
    elif x == 0:
        return str_x[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(str_x[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

