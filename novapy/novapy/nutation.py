from novapy.dynamical_time import ln_get_jde
from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_range_degrees

from math import sin
from math import cos



class NutationArguments:
    D = float()
    M = float()
    MM = float()
    F = float()
    O = float()

    def __init__(self, d, m, mM, f, o):
        self.D = d
        self.M = m
        self.MM = mM
        self.F = f
        self.O = o




arguments = [
    NutationArguments(0.0, 0.0, 0.0, 0.0, 1.0),
    NutationArguments(-2.0, 0.0, 0.0, 2.0, 2.0),
    NutationArguments(0.0, 0.0, 0.0, 2.0, 2.0),
    NutationArguments(0.0, 0.0, 0.0, 0.0, 2.0),
    NutationArguments(0.0, 1.0, 0.0, 0.0, 0.0),
    NutationArguments(0.0, 0.0, 1.0, 0.0, 0.0),
    NutationArguments(-2.0, 1.0, 0.0, 2.0, 2.0),
    NutationArguments(0.0, 0.0, 0.0, 2.0, 1.0),
    NutationArguments(0.0, 0.0, 1.0, 2.0, 2.0),
    NutationArguments(-2.0, -1.0, 0.0, 2.0, 2.0),
    NutationArguments(-2.0, 0.0, 1.0, 0.0, 0.0),
    NutationArguments(-2.0, 0.0, 0.0, 2.0, 1.0),
    NutationArguments(0.0, 0.0, -1.0, 2.0, 2.0),
    NutationArguments(2.0, 0.0, 0.0, 0.0, 0.0),
    NutationArguments(0.0, 0.0, 1.0, 0.0, 1.0),
    NutationArguments(2.0, 0.0, -1.0, 2.0, 2.0),
    NutationArguments(0.0, 0.0, -1.0, 0.0, 1.0),
    NutationArguments(0.0, 0.0, 1.0, 2.0, 1.0),
    NutationArguments(-2.0, 0.0, 2.0, 0.0, 0.0),
    NutationArguments(0.0, 0.0, -2.0, 2.0, 1.0),
    NutationArguments(2.0, 0.0, 0.0, 2.0, 2.0),
    NutationArguments(0.0, 0.0, 2.0, 2.0, 2.0),
    NutationArguments(0.0, 0.0, 2.0, 0.0, 0.0),
    NutationArguments(-2.0, 0.0, 1.0, 2.0, 2.0),
    NutationArguments(0.0, 0.0, 0.0, 2.0, 0.0),
    NutationArguments(-2.0, 0.0, 0.0, 2.0, 0.0),
    NutationArguments(0.0, 0.0, -1.0, 2.0, 1.0),
    NutationArguments(0.0, 2.0, 0.0, 0.0, 0.0),
    NutationArguments(2.0, 0.0, -1.0, 0.0, 1.0),
    NutationArguments(-2.0, 2.0, 0.0, 2.0, 2.0),
    NutationArguments(0.0, 1.0, 0.0, 0.0, 1.0),
    NutationArguments(-2.0, 0.0, 1.0, 0.0, 1.0),
    NutationArguments(0.0, -1.0, 0.0, 0.0, 1.0),
    NutationArguments(0.0, 0.0, 2.0, -2.0, 0.0),
    NutationArguments(2.0, 0.0, -1.0, 2.0, 1.0),
    NutationArguments(2.0, 0.0, 1.0, 2.0, 2.0),
    NutationArguments(0.0, 1.0, 0.0, 2.0, 2.0),
    NutationArguments(-2.0, 1.0, 1.0, 0.0, 0.0),
    NutationArguments(0.0, -1.0, 0.0, 2.0, 2.0),
    NutationArguments(2.0, 0.0, 0.0, 2.0, 1.0),
    NutationArguments(2.0, 0.0, 1.0, 0.0, 0.0),
    NutationArguments(-2.0, 0.0, 2.0, 2.0, 2.0),
    NutationArguments(-2.0, 0.0, 1.0, 2.0, 1.0),
    NutationArguments(2.0, 0.0, -2.0, 0.0, 1.0),
    NutationArguments(2.0, 0.0, 0.0, 0.0, 1.0),
    NutationArguments(0.0, -1.0, 1.0, 0.0, 0.0),
    NutationArguments(-2.0, -1.0, 0.0, 2.0, 1.0),
    NutationArguments(-2.0, 0.0, 0.0, 0.0, 1.0),
    NutationArguments(0.0, 0.0, 2.0, 2.0, 1.0),
    NutationArguments(-2.0, 0.0, 2.0, 0.0, 1.0),
    NutationArguments(-2.0, 1.0, 0.0, 2.0, 1.0),
    NutationArguments(0.0, 0.0, 1.0, -2.0, 0.0),
    NutationArguments(-1.0, 0.0, 1.0, 0.0, 0.0),
    NutationArguments(-2.0, 1.0, 0.0, 0.0, 0.0),
    NutationArguments(1.0, 0.0, 0.0, 0.0, 0.0),
    NutationArguments(0.0, 0.0, 1.0, 2.0, 0.0),
    NutationArguments(0.0, 0.0, -2.0, 2.0, 2.0),
    NutationArguments(-1.0, -1.0, 1.0, 0.0, 0.0),
    NutationArguments(0.0, 1.0, 1.0, 0.0, 0.0),
    NutationArguments(0.0, -1.0, 1.0, 2.0, 2.0),
    NutationArguments(2.0, -1.0, -1.0, 2.0, 2.0),
    NutationArguments(0.0, 0.0, 3.0, 2.0, 2.0),
    NutationArguments(2.0, -1.0, 0.0, 2.0, 2.0)]

class NutationCoefficients:
    longitude1 = float()
    longitude2 = float()
    obliquity1 = float()
    obliquity2 = float()


    
    def __init__(self, lon1, lon2, ob1, ob2):
        self.longitude1 = lon1
        self.longitude2 = lon2
        self.obliquity1 = ob1
        self.obliquity2 = ob2

coeficients = [
    NutationCoefficients(-171996.0, -174.2, 92025.0, 8.9),
    NutationCoefficients(-13187.0, -1.6, 5736.0, -3.1),
    NutationCoefficients(-2274.0, -0.2, 977.0, -0.5),
    NutationCoefficients(2062.0, 0.2, -895.0, 0.5),
    NutationCoefficients(1426.0, -3.4, 54.0, -0.1),
    NutationCoefficients(712.0, 0.1, -7.0, 0.0),
    NutationCoefficients(-517.0, 1.2, 224.0, -0.6),
    NutationCoefficients(-386.0, -0.4, 200.0, 0.0),
    NutationCoefficients(-301.0, 0.0, 129.0, -0.1),
    NutationCoefficients(217.0, -0.5, -95.0, 0.3),
    NutationCoefficients(-158.0, 0.0, 0.0, 0.0),
    NutationCoefficients(129.0, 0.1, -70.0, 0.0),
    NutationCoefficients(123.0, 0.0, -53.0, 0.0),
    NutationCoefficients(63.0, 0.0, 0.0, 0.0),
    NutationCoefficients(63.0, 0.1, -33.0, 0.0),
    NutationCoefficients(-59.0, 0.0, 26.0, 0.0),
    NutationCoefficients(-58.0, -0.1, 32.0, 0.0),
    NutationCoefficients(-51.0, 0.0, 27.0, 0.0),
    NutationCoefficients(48.0, 0.0, 0.0, 0.0),
    NutationCoefficients(46.0, 0.0, -24.0, 0.0),
    NutationCoefficients(-38.0, 0.0, 16.0, 0.0),
    NutationCoefficients(-31.0, 0.0, 13.0, 0.0),
    NutationCoefficients(29.0, 0.0, 0.0, 0.0),
    NutationCoefficients(29.0, 0.0, -12.0, 0.0),
    NutationCoefficients(26.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-22.0, 0.0, 0.0, 0.0),
    NutationCoefficients(21.0, 0.0, -10.0, 0.0),
    NutationCoefficients(17.0, -0.1, 0.0, 0.0),
    NutationCoefficients(16.0, 0.0, -8.0, 0.0),
    NutationCoefficients(-16.0, 0.1, 7.0, 0.0),
    NutationCoefficients(-15.0, 0.0, 9.0, 0.0),
    NutationCoefficients(-13.0, 0.0, 7.0, 0.0),
    NutationCoefficients(-12.0, 0.0, 6.0, 0.0),
    NutationCoefficients(11.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-10.0, 0.0, 5.0, 0.0),
    NutationCoefficients(-8.0, 0.0, 3.0, 0.0),
    NutationCoefficients(7.0, 0.0, -3.0, 0.0),
    NutationCoefficients(-7.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-7.0, 0.0, 3.0, 0.0),
    NutationCoefficients(-7.0, 0.0, 3.0, 0.0),
    NutationCoefficients(6.0, 0.0, 0.0, 0.0),
    NutationCoefficients(6.0, 0.0, -3.0, 0.0),
    NutationCoefficients(6.0, 0.0, -3.0, 0.0),
    NutationCoefficients(-6.0, 0.0, 3.0, 0.0),
    NutationCoefficients(-6.0, 0.0, 3.0, 0.0),
    NutationCoefficients(5.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-5.0, 0.0, 3.0, 0.0),
    NutationCoefficients(-5.0, 0.0, 3.0, 0.0),
    NutationCoefficients(-5.0, 0.0, 3.0, 0.0),
    NutationCoefficients(4.0, 0.0, 0.0, 0.0),
    NutationCoefficients(4.0, 0.0, 0.0, 0.0),
    NutationCoefficients(4.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-4.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-4.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-4.0, 0.0, 0.0, 0.0),
    NutationCoefficients(3.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-3.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-3.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-3.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-3.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-3.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-3.0, 0.0, 0.0, 0.0),
    NutationCoefficients(-3.0, 0.0, 0.0, 0.0)]

LN_NUTATION_EPOCH_THRESHOLD = 0.1


#  Calculate nutation of longitude and obliquity in degrees from Julian
#  Ephemeris Day

def ln_get_nutation(jddoule, nutation):
    JD = jddoule
    c_JD = 0.0
    c_longitude = 0.0
    c_obliquity = 0.0
    c_ecliptic = 0.0

    t1 = compare_to(abs(c_JD), LN_NUTATION_EPOCH_THRESHOLD)

    if t1 > 0:
        c_JD = JD
        JDE = ln_get_jde(JD)
        t = (JDE - 2451545.0) / 36525.0
        t2 = t * t
        t3 = t2 * t

        d = ((297.85036 + (445267.111480 * t)) - (0.0019142 * t2)) + (t3 / 189474)
        m = ((357.52772 + (35999.050340 * t)) - (0.0001603 * t2)) - (t3 - 300000)
        mm = ((134.96298 + (477198.867398 * t)) + (0.0086972 * t2)) + (t3 / 56250)
        f = ((93.2719100 + (483202.017538 * t)) - (0.0036825 * t2)) + (t3 / 327270)
        o = ((125.04452 - (1934.136261 * t)) + (0.0020708 * t2)) + (t3 / 450000)

        d = ln_deg_to_rad(d)
        m = ln_deg_to_rad(m)
        mm = ln_deg_to_rad(mm)
        f = ln_deg_to_rad(f)
        o = ln_deg_to_rad(o)

        idx = 0
        #  calc sum of terms in table 21A
        for i in arguments:
            #  calc coefficients of sine and cosine
            coef_sine = coeficients[idx].longitude1 + (coeficients[idx].longitude2 * t)
            coef_cos = coeficients[idx].obliquity1 + (coeficients[idx].obliquity2 * t)
            argument = ((((i.D * d) + (i.M * m)) + (i.MM * mm)) + (i.F * f)) + (i.O * o)

            c_longitude = c_longitude + (coef_sine * sin(argument))
            c_obliquity = c_obliquity + (coef_cos * cos(argument))

        #  change to arcsecs
        c_longitude = c_longitude / 10000
        c_obliquity = c_obliquity / 10000

        #  change to degrees
        c_longitude = c_longitude / (60 * 60)
        c_obliquity = c_obliquity / (60 * 60)


        #  calculate mean ecliptic - Meeus 2nd edition, eq. 22.2
        c_ecliptic = (((((23 + (26 / 60)) + (21.448 / 3600)) -
                            ((46.8150 / 3600) * t)) -
                            ((0.00059 / 3600) * t2)) +
                            ((0.001813 / 3600) * t3))


    longitude = c_longitude
    obliquity = c_obliquity
    ecliptic = c_ecliptic




def compare_to( a, b):
    return (a > b) - (a < b)