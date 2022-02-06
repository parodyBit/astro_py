from enum import Enum
from decimal import Decimal
from math import pi
from math import sqrt
import re
from novapy.api.ln_dms import LnDms
from novapy.api.ln_hms import LnHms
from novapy.util.tokens import Tokens


class Type(Enum):
    HOURS = 1
    DEGREES = 2
    LAT = 3
    LONG = 4


class Utility:
    def __init__(self):
        pass


D2R = 0.017453292519943295769

#  radian.deg
R2D = 5.7295779513082320877


def ln_get_version():
    # load properties, from .ini ?
    return '0.0.1'


def ln_rad_to_deg(radians):
    #  Convert radians to degrees
    return radians * R2D


def ln_deg_to_rad(degrees):
    #  Convert degrees to radians
    return degrees * D2R


def ln_hms_to_deg(hms):
    #  Convert hours:mins:secs to degrees
    degrees = (hms.hours / 24) * 360
    degrees += (hms.minutes / 60) * 15.
    degrees += (hms.seconds / 60) * 0.25
    return degrees


def ln_hms_to_rad(hms):
    # convert hours:mins:secs to radians
    radians = (hms.hours / 24.) * 2. * pi
    radians += (hms.minutes / 60.) * 2. * pi / 24.
    radians += (hms.seconds / 60.) * 2. * pi / 1440.
    return radians


def ln_deg_to_hms(degrees, hms):
    #  puts a large angle in the correct range 0 - 360 degrees
    degrees = ln_range_degrees(degrees)

    #  divide degrees by 15 to get the hours
    dtemp = degrees / 15
    hms.hours = int(dtemp)

    #  multiply remainder by 60 to get minutes
    dtemp = 60 * (dtemp - hms.hours)
    hms.minutes = int(dtemp)

    #  multiply remainder by 60 to get seconds
    hms.seconds = int(60 * (dtemp - hms.minutes))

    #  catch any overflows
    if hms.seconds > 59:
        hms.seconds = 0
        hms.minutes += 1
    if hms.minutes > 59:
        hms.minutes = 0
        hms.hours += 1


def ln_rad_to_hms(radians, hms):
    #  convert radians to hh:mm:ss
    radians = ln_range_radians(radians)
    degrees = ln_rad_to_deg(radians)
    ln_deg_to_hms(degrees, hms)


def ln_dms_to_deg(dms):
    #  convert dms to degrees
    degrees = abs(float(dms.degrees))
    degrees += abs(dms.minutes / 60.)
    degrees += abs(dms.seconds / 3600.)
    # negative ?
    if dms.neg != 0:
        degrees *= -1.0
    return degrees


def ln_dms_to_rad(dms):
    #  convert dms to radians
    radians = abs(dms.degrees / 360. * 2. * pi)
    radians += abs(dms.minutes / 21600. * 2. * pi)
    radians += abs(dms.seconds / 1296000. * 2. * pi)
    # negative ?
    if dms.neg != 0:
        radians *= -1.0
    return radians


def ln_deg_to_dms(degrees, dms):
    #  convert degrees to dms
    if degrees >= 0:
        dms.neg = 0
    else:
        dms.neg = 1
    degrees = abs(degrees)
    dms.degrees = int(degrees)
    # multiply remainder by 60 to get minutes
    dtemp = 60. * (degrees - dms.degrees)
    dms.minutes = int(dtemp)
    dms.seconds = int(60. * (dtemp - dms.minutes))
    # catch any overflows
    if dms.seconds > 59:
        dms.seconds = 0.0
        dms.minutes += 1
    if dms.minutes > 59:
        dms.minutes = 0
        dms.degrees += 1


def ln_rad_to_dms(radians, dms):
    #  convert radians to dms
    degrees = ln_rad_to_deg(radians)
    ln_deg_to_dms(degrees, dms)


def ln_range_degrees(angle):
    #  puts a large angle in the correct range 0 - 360 degrees
    if 0. <= angle < 360.0:
        return angle
    temp = int(angle / 360)
    if angle < 0.0:
        temp -= 1
    temp *= 360.0
    return angle - temp


def ln_range_radians(angle):
    #  puts a large angle in the correct range 0 - 2PI radians
    if 0. <= angle < (2 * pi):
        return angle
    temp = int(angle/(pi*2))
    if angle < 0.0:
        temp -= 1
    temp *= (pi * 2.)
    return angle - temp



def ln_range_radians2(angle):
    #  puts a large angle in the correct range -2PI - 2PI radians
    #  preserve sign
    if (-2. * pi) < angle < (2. * pi):
        return angle
    temp = int(angle / (pi * 2.))
    temp = temp * (pi * 2)
    return angle - temp


def ln_add_secs_hms(hms, seconds):
    #  add seconds to hms
    source_hms = LnHms()
    source_hms.hours = int(seconds / 3600)
    seconds -= source_hms.hours * 3600
    source_hms.minutes = int(seconds / 60)
    seconds -= source_hms.minutes * 60
    source_hms.seconds = seconds
    ln_add_hms(source_hms, hms)

def ln_add_hms(source, dest):
    #  add hms to hms
    dest.seconds += source.seconds
    if dest.seconds >= 60.0:
        source.minutes += 1
        dest.seconds -= 60.0
    else:
        if dest.seconds < 0.0:
            source.minutes -= 1
            dest.seconds += 60.0
    dest.minutes += source.minutes
    if dest.minutes >= 60:
        source.hours += 1
        dest.minutes -= 60
    else:
        if dest.seconds < 0.0:
            source.hours -= 1
            dest.minutes += 60
    dest.hours += source.hours


def ln_hequ_to_equ(hpos, pos):
    #  equatorial position to double equatorial position
    pos.ra = ln_hms_to_deg(hpos.ra)
    pos.dec = ln_dms_to_deg(hpos.dec)


def ln_equ_to_hequ(pos, hpos):
    #  equatorial position to human readable equatorial position
    ln_deg_to_hms(pos.ra, hpos.ra)
    ln_deg_to_dms(pos.dec, hpos.dec)


def ln_hhrz_to_hrz(hpos, pos):
    #  horizontal position to double horizontal position
    pos.alt = ln_dms_to_deg(hpos.alt)
    pos.az = ln_dms_to_deg(hpos.az)


def ln_hrz_to_hhrz(pos, hpos):
    #  horizontal position to human readable horizontal position
    ln_deg_to_dms(pos.alt, hpos.alt)
    ln_deg_to_dms(pos.az, hpos.az)


def ln_hrz_to_nswe(pos):
    #  position of given azimuth - like N,S,W,E,NSW,...
    directions = ['S', 'SSW', 'SW', 'SWW', 'W', 'NWW', 'NW', 'NNW', 'N', 'NNE', 'NE', 'NEE', 'E', 'SEE', 'SE', 'SSE']
    return directions[int(pos.az/22.5)]



def ln_lnlat_to_hlnlat(lnlat_pos, hlnlat_pos):
    #  long/lat position to human readable long/lat position
    ln_deg_to_dms(lnlat_pos.lng, hlnlat_pos.lng)
    ln_deg_to_dms(lnlat_pos.lat, hlnlat_pos.lat)


def ln_hlnlat_to_lnlat(hlnlat_pos, lnlat_pos):
    ln_deg_to_dms(lnlat_pos.lng, hlnlat_pos.lng)
    ln_deg_to_dms(lnlat_pos.lat, hlnlat_pos.lat)


def ln_get_rect_distance(a, b):
    #  Calculate the distance between rectangular points a and b.
    x = a.X - b.X
    y = a.Y - b.Y
    z = a.Z = b.Z

    x *= x
    y *= y
    z *= z

    return sqrt(x + y + z)


def ln_get_light_time(dist):
    #  Convert units of AU into Light Days
    return dist * 0.005775183


def trim(string):
    #  remove whitespace from end of string
    return str(string.rstrip())

def ln_get_dec_location(string):
    '''
      Obtains Latitude, Longitude, RA or Declination from a string.
      If the last char is N/S doesn't accept more than 90 degrees,
      If it is E/W doesn't accept more than 180 degrees.
      If they are hours don't accept more than 24:00

     Any position can be expressed as follows:
       (please use a 8 bits charset if you want to view the degrees separator char '0xba')
      42.30.35,53 90º0'0,01 W 42º30'35.53 N 42º30'35.53S 42º30'N - 42.30.35.53
      42:30:35.53 S + 42.30.35.53 +42º30 35,53 23h36'45,0
      42:30:35.53 S = -42º30'35.53" + 42 30.35.53 S the same previous position,
      the plus (+) sign is considered like an error, the last 'S' has
      precedence over the sign

      90º0'0,01 N ERROR: +- 90º0'00.00" latitude limit
    '''
    ptr = str()
    negative = bool(False)
    delim1 = [' ', ':', '.', ',', ';', 'D', 'd', 'H', 'h', 'M', 'm', '\n', '\t']
    delim2 = [' ', 'N', 'S', 'E', 'W', 'n', 's', 'e', 'w']
    dghh = int(0)
    minutes = int(0)
    seconds = float(0.)
    pos = float()

    if not string:
        return -0.0

    ptrIndex = int(0)

    ptr = trim(string)
    if ptr[ptrIndex] == '+' or ptr[ptrIndex] == '-':
        ptrIndex += 1
        negative = True if ptr[ptrIndex] == '-' else negative
    type = Type
    ptr = ptr[ptrIndex:]
    ame = index_one_of(ptr, 'S', 's', 'N', 'n')

    hh = index_one_of(ptr, 'H', 'h')
    if 0 <= hh < 3:
        type = Type.HOURS
        if negative:
            # if RA no negative numbers
            negative = False
    elif ame >= 0:
        type = Type.LAT
        if ame == 0:
            ptr = ptr[1:]
    else:
        type = Type.DEGREES

    tokens = Tokens(ptr, delim1)
    temp = tokens.next_token(delim1)
    if temp is not None:
        ptr = temp
        dghh = int(ptr)
    else:
        return -0.0
    temp = tokens.next_token(delim1)
    if temp is not None:
        ptr = temp
        minutes = int(ptr)
        if minutes > 59:
            return -0.0
    else:
        return -0.0
    temp = tokens.next_token(delim2)
    if temp is not None:
        ptr = temp
        ptr.replace(',', '.')
        seconds = float(ptr[1])
        if seconds >= 60.0:
            return -0.0
    temp = tokens.next_token(to_char_array(' \n\t'))
    if temp is not None:
        ptr = temp
        ptr = trim(ptr)
        if ptr[0] == 'S' or ptr[0] == 'W' or ptr[0] == 's' or ptr[0] == 'w':
            negative = True

    pos = dghh + minutes / 60. + seconds / 3600.0
    if type == Type.HOURS and pos > 24:
        return -0.0
    if type == Type.LAT and pos > 90:
        return -0.0
    if negative:
        pos = 0. - pos
    return pos



def ln_get_humanr_location(location):
    #  Obtains a human readable location in the form: ddºmm'ss.ss"
    n1 = location / 1.
    n2 = location % 1.
    deg = location / 1.
    sec = 60 * (location % 1.)
    if sec < 0:
        sec *= -1.
    min = sec / 1
    sec = 60 * (location % 1.)
    val = '{:.0f}º {:.0f}\' {:.0f}\"'
    return val.format(deg,min,sec)


def ln_interpolate3(n, y1, y2, y3):
    #  Calculate an intermediate value of the 3 arguments for the given
    #  interpolation factor.
    a = y2 - y1
    b = y3 - y2
    c = b - a

    y = y2 + n / 2. * (a + b + n * c)
    return y

#  Calculate an intermediate value of the 5 arguments for the given
#  interpolation factor.


def ln_interpolate5(n, y1, y2, y3, y4, y5):

    A = y2 - y1
    B = y3 - y2
    C = y4 - y3
    D = y5 - y4
    E = B - A
    F = C - B
    G = D - C
    H = F - E
    J = G - F
    K = J - H

    y = 0.0

    n2 = n * n
    n3 = n2 * n
    n4 = n3 * n

    y += y3
    y += n * ((B + C) / 2. - (H + J) / 12.)
    y += n2 * (F / 2. - K / 24.)
    y += n3 * ((H + J) / 12.)
    y += n4 * (K / 24)

    return y

def cbrt(x):
    #  Simple cube root
    return x ** (1./3.)


def nan(string):
    return None


def to_char_array(string):
    char_array = []
    for c in string:
        char_array.append(c)
    return char_array

def index_one_of(string, *args):

    idx = 0
    for arg in args:
        for i,c in enumerate(string):
            if arg == c:
                return i
    return -1
