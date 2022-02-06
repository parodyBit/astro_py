


class year_TD:
    year = int
    TD = float
    def __init__(self):
        pass



#  dynamical time in seconds for every second year from 1620 to 1992
delta_t = [
    124.0, 115.0, 106.0, 98.0, 91.0,
    85.0, 79.0, 74.0, 70.0, 65.0, 62.0, 58.0, 55.0, 53.0, 50.0, 48.0,
    46.0, 44.0, 42.0, 40.0, 37.0, 35.0, 33.0, 31.0, 28.0, 26.0, 24.0,
    22.0, 20.0, 18.0, 16.0, 14.0, 13.0, 12.0, 11.0, 10.0, 9.0, 9.0,
    9.0, 9.0, 9.0, 9.0, 9.0, 9.0, 10.0, 10.0, 10.0, 10.0, 10.0, 11.0,
    11.0, 11.0, 11.0, 11.0, 11.0, 11.0, 12.0, 12.0, 12.0, 12.0, 12.0,
    12.0, 13.0, 13.0, 13.0, 13.0, 14.0, 14.0, 14.0, 15.0, 15.0, 15.0,
    15.0, 16.0, 16.0, 16.0, 16.0, 16.0, 17.0, 17.0, 17.0, 17.0, 17.0,
    17.0, 17.0, 17.0, 16.0, 16.0, 15.0, 14.0, 13.7, 13.1, 12.7, 12.5,
    12.5, 12.5, 12.5, 12.5, 12.5, 12.3, 12.0, 11.4, 10.6, 9.6, 8.6,
    7.5, 6.6, 6.0, 5.7, 5.6, 5.7, 5.9, 6.2, 6.5, 6.8, 7.1, 7.3, 7.5,
    7.7, 7.8, 7.9, 7.5, 6.4, 5.4, 2.9, 1.6, -1.0, -2.7, -3.6, -4.7,
    -5.4, -5.2, -5.5, -5.6, -5.8, -5.9, -6.2, -6.4, -6.1, -4.7, -2.7,
    0.0, 2.6, 5.4, 7.7, 10.5, 13.4, 16.0, 18.2, 20.2, 21.2, 22.4, 23.5,
    23.9, 24.3, 24.0, 23.9, 23.9, 23.7, 24.0, 24.3, 25.3, 26.2, 27.3,
    28.2, 29.1, 30.0, 30.7, 31.4, 32.2, 33.1, 34.0, 35.0, 36.5, 38.3,
    40.2, 42.2, 44.5, 46.5, 48.5, 50.5, 52.2, 53.8, 54.9, 55.8, 56.9,
    58.3]

#  Stephenson and Houlden for years prior to 948 A.D.

def get_dynamical_diff_sh1(jd):
    E = (jd - 2067314.5) / 36525.0
    TD = 1830.0 - 405.0 * E + 46.5 * E * E
    return TD

#  Stephenson and Houlden for years between 948 A.D. and 1600 A.D.

def get_dynamical_diff_sh2(jd):
    # number of centuries from 1850
    t = (jd - 2396758.5) / 36525.0
    TD = 22.5 * t * t
    return TD

#   for years 1600..1992

def get_dynamical_diff_table(jd):

    # get no days since 1620 and divide by 2 years
    i = int((jd-2312752.5) / 730.5)
    if i > delta_t.__sizeof__() - 2:
        # get the base interpolation factor in the table
        i = delta_t.__sizeof__() - 2

    a = delta_t[i + 1] - delta_t[i]
    b = delta_t[i + 2] - delta_t[i + 1]
    c = a - b
    n = ((jd - (2312752.5 + (730.5 * i))) / 730.5)

    TD = delta_t[i + 1] + n / 2 * (a + b + n * c)
    return TD

def get_dynamical_diff_near(jd):

    # TD for 1990, 2000, 2010
    delta_T = [56.86, 63.83, 70]
    a = delta_T[1]-delta_T[0]
    b = delta_T[2] - delta_T[1]
    c = b - a

    # get number of days since 2000 and divide by 10 years
    n = (jd - 2451544.5) / 3652.5
    TD = delta_T[1] + (n / 2) * (a + b + n * c)
    return TD

# other JD values

def get_dynamical_diff_other(jd):
    a = (jd - 2382148.0)
    a *= a
    TD = -15.0 + a / 41048480.0
    return TD

def ln_get_dynamical_time_diff(jd):
    if jd < 2067314.5:
        TD = get_dynamical_diff_sh1(jd)
    elif 2067314.5 <= jd < 2305447.5:
        # check for date 948..1600 A.D. Stephenson and Houlden
        TD = get_dynamical_diff_sh2(jd)
    elif 2312752.5 <= jd < 2448622.5:
        #  check for value in table 1620..1992 interpolation of table */
        TD = get_dynamical_diff_table(jd)
    elif 2448622.5 <= jd <= 2455197.5:
        # check for near future 1992..2010 interpolation
        TD = get_dynamical_diff_near(jd)
    else:
        # other time period outside
        TD = get_dynamical_diff_other(jd)
    return TD

#  Calculates the Julian Ephemeris Day(JDE) from the given julian day

def ln_get_jde(jd):
    secs_in_day = 24 * 60 * 60.0
    JDE = jd + ln_get_dynamical_time_diff(jd) / secs_in_day
    return JDE
