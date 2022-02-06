

import csv
from math import pi
from math import sin
from math import atan2
from math import cos
from math import sqrt
from math import acos
from math import exp
from math import e
from novapy.api.ln_equ_posn import LnEquPosn
from novapy.api.ln_rect_posn import LnRectPosn
from novapy.api.ln_lnlat_posn import LnLnlatPosn
from novapy.solar_system.solar import ln_get_solar_equ_coords
from novapy.solar_system.solar import ln_get_solar_ecl_coords
from novapy.solar_system.earth import ln_get_earth_solar_dist
from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_range_radians2
from novapy.utility import ln_range_radians
from novapy.riseset import ln_get_body_rst_horizon
from novapy.utility import ln_range_degrees
from novapy.transform import ln_get_equ_from_ecl

#precision

LN_LUNAR_STANDARD_HORIZON = 0.125
# AU in KM
AU = 149597870
# Lunar Constants (move to Constants.py ? )
RAD = (648000.0 / pi)
DEG = (pi / 180.0)
M_PI_2 = (pi / 2.0)
PIS2 = (pi / 2.0)
ATH = 384747.9806743165
A0 = 384747.9806448954
AM = 0.074801329518
ALPHA = 0.002571881335
DTASM = (2.0 * ALPHA / (3.0 * AM))
W12 = (1732559343.73604 / RAD)
PRECES = (5029.0966 / RAD)
C1 = 60.0
C2 = 3600.0

DELNU = ((0.55604 / RAD) / W12)
DELE = (0.01789 / RAD)
DELG = (-0.08066 / RAD)
DELNP = ((-0.06424 / RAD) / W12)
DELEP = (-0.12879 / RAD)

P1 = 0.10180391e-4
P2 = 0.47020439e-6
P3 = -0.5417367e-9
P4 = -0.2507948e-11
P5 = 0.463486e-14
Q1 = -0.113469002e-3
Q2 = 0.12372674e-6
Q3 = 0.1265417e-8
Q4 = -0.1371808e-11
Q5 = -0.320334e-14



W1 = [(218.0 + (18.0 / 60.0) + (59.95571 / 3600.0)) * DEG,
      1732559343.73604 / RAD,
      -5.8883 / RAD,
      0.006604 / RAD,
      -0.00003169 / RAD]
W2 = [(83.0 + (21.0 / 60.0) + (11.67475 / 3600.0)) * DEG,
      14643420.2632 / RAD,
      -38.2776 / RAD,
      -0.045047 / RAD,
      0.00021301 / RAD]
W3 = [(125.0 + (2.0 / 60.0) + (40.39816 / 3600.0)) * DEG,
      -6967919.3622 / RAD,
      6.3622 / RAD,
      0.007625 / RAD,
      -0.00003586 / RAD]
earth = [(100.0 + (27.0 / 60.0) + (59.22059 / 3600.0)) * DEG,
         129597742.2758 / RAD,
         -0.0202 / RAD,
         0.000009 / RAD,
         0.00000015 / RAD]

peri = [(102.0 + (56.0 / 60.0) + (14.42753 / 3600.0)) * DEG,
        1161.2283 / RAD,
        0.5327 / RAD,
        -0.000138 / RAD,
        0]
d1 = [5.198466741027443, 7771.377146811758394, -0.000028449351621, 0.000000031973462, -0.000000000154365]
d2 = [-0.043125180208125, 628.301955168488007, -0.000002680534843, 0.000000000712676, 0.000000000000727]
d3 = [2.355555898265799, 8328.691426955554562, 0.000157027757616, 0.000000250411114, -0.000000001186339]
d4 = [1.627905233371468, 8433.466158130539043, -0.000059392100004, -0.000000004949948, 0.000000000020217]
delt = [d1, d2, d3, d4]

p1 = [(252 + 15 / C1 + 3.25986 / C2) * DEG, 538101628.68898 / RAD]
p2 = [(181 + 58 / C1 + 47.28305 / C2) * DEG, 210664136.43355 / RAD]
p3 = [(100.0 + (27.0 / 60.0) + (59.22059 / 3600.0)) * DEG, 129597742.2758 / RAD]
p4 = [(355 + 25 / C1 + 59.78866 / C2) * DEG, 68905077.59284 / RAD]
p5 = [(34 + 21 / C1 + 5.34212 / C2) * DEG, 10925660.42861 / RAD]
p6 = [(50 + 4 / C1 + 38.89694 / C2) * DEG, 4399609.65932 / RAD]
p7 = [(314 + 3 / C1 + 18.01841 / C2) * DEG, 1542481.19393 / RAD]
p8 = [(304 + 20 / C1 + 55.19575 / C2) * DEG, 786550.32074 / RAD]
p = [p1, p2, p3, p4, p5, p6, p7, p8]

zeta = [(218.0 + (18.0 / 60.0) + (59.95571 / 3600.0)) * DEG, ((1732559343.73604 / RAD) + PRECES)]
def get_int_list(list):
    int_list = []
    for item in list:
        int_list.append(int(item))
    return int_list

def get_float_list(list):
    float_list = []
    for item in list:
        float_list.append(float(item))
    return float_list


class MainProblem:
    ilu = []
    a = 0
    b = []
    def __init__(self, ilu, a, b):
        self.ilu = ilu
        self.a = a
        self.b = b


    def to_str(self):
        return '[{0},{1},{2}]'.format(self.ilu, self.a, self.b)

    def __init__(self, line):
        #print('b = ', self.b)

        parts = line.split(',')

        ilu_slice = slice(0, 4)  # first 4 values

        b_slice = slice(5, 10)  # next 5 values
        self.ilu = get_int_list(parts[ilu_slice])
        self.a = float(parts[4])
        self.b = get_float_list(parts[b_slice])
        #print(self.to_str())
        #print('ilu = ', self.ilu)
        ##print('a = ', self.a)



class EarthPart:
    iz = 0
    ilu = []
    o = 0
    a = 0
    p = 0

    def to_str(self):
        return '[iz = {0}, ilu = {1}, o = {2}, a = {3}, p = {4}]'.format(self.iz, self.ilu, self.o, self.a, self.p)

    def __init__(self, iz, ilu, o, a, p):
        self.iz = iz
        self.ilu = ilu
        self.o = o
        self.a = a
        self.p = p


    def __init__(self, line):
        parts = line.split(',')
        self.iz = int(parts[0])
        # print(parts)
        ilu_slice = slice(1, 5)  # first 4 values
        self.ilu = get_int_list(parts[ilu_slice])

        self.o = float(parts[5])
        self.a = float(parts[6])
        self.p = float(parts[7])
        #print(self.to_str())

class PlanetPart:
    ipla = []
    theta = 0.
    o = 0.
    p = 0.

    def to_str(self):
        return '[ipla = {0}, theta = {1}, o = {2}, p = {3}]'.format(self.ipla, self.theta, self.o, self.p)

    def __init__(self, ipla, theta, o, p):
        self.ipla = ipla
        self.theta = theta
        self.o = o
        self.p = p

    def __init__(self, line):
        parts = line.split(',')
        ipla_slice = slice(0, 11)
        self.ipla = get_int_list(parts[ipla_slice])
        self.theta = float(parts[11])
        self.o = float(parts[12])
        self.p = float(parts[13])
        #print(self.to_str())

class TidalEffects(EarthPart):

    def __init__(self, iz, ilu, o, a, p):
        EarthPart.__init__(iz, ilu, o, a, p)

    def __init__(self, line):
        EarthPart.__init__(self, line)


class MoonPart(EarthPart):
    def __init__(self, iz, ilu, o, a, p):
        EarthPart.__init__(iz, ilu, o, a, p)

    def __init__(self, line):
        EarthPart.__init__(self, line)



class RelPart(EarthPart):
    def __init__(self, iz, ilu, o, a, p):
        EarthPart.__init__(iz, ilu, o, a, p)

    def __init__(self, line):
        EarthPart.__init__(self, line)


class SolPart(EarthPart):
    def __init__(self, iz, ilu, o, a, p):
        EarthPart.__init__(iz, ilu, o, a, p)

    def __init__(self, line):
        EarthPart.__init__(self, line)



elp1_main = []
elp2_main = []
elp3_main = []
elp4_earth_pert = []
elp5_earth_pert = []
elp6_earth_pert = []
elp7_earth_pert = []
elp8_earth_pert = []
elp9_earth_pert = []
elp10_planet_pert = []
elp11_planet_pert = []
elp12_planet_pert = []
elp13_planet_pert = []
elp14_planet_pert = []
elp15_planet_pert = []
elp16_planet_pert = []
elp17_planet_pert = []
elp18_planet_pert = []
elp19_planet_pert = []
elp20_planet_pert = []
elp21_planet_pert = []
elp22_tidal_pert = []
elp23_tidal_pert = []
elp24_tidal_pert = []
elp25_tidal_pert = []
elp26_tidal_pert = []
elp27_tidal_pert = []
elp28_moon_pert = []
elp29_moon_pert = []
elp30_moon_pert = []
elp31_rel_pert = []
elp32_rel_pert = []
elp33_rel_pert = []
elp34_sol_pert = []
elp35_sol_pert = []
elp36_sol_pert = []

def load_data():
    file = open('novapy/solar_system/lunar/elp1_main.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp1_main.append(MainProblem(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp2_main.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp2_main.append(MainProblem(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp3_main.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp3_main.append(MainProblem(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp4_earth_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp4_earth_pert.append(EarthPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp5_earth_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp5_earth_pert.append(EarthPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp6_earth_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp6_earth_pert.append(EarthPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp7_earth_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp7_earth_pert.append(EarthPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp8_earth_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp8_earth_pert.append(EarthPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp9_earth_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp9_earth_pert.append(EarthPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp10_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp10_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp11_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp11_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp12_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp12_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp13_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp13_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp14_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp14_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp15_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp15_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp16_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp16_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp17_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp17_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp18_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp18_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp19_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp19_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp20_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp20_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp21_planet_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp21_planet_pert.append(PlanetPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp22_tidal_effects.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp22_tidal_pert.append(TidalEffects(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp23_tidal_effects.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp23_tidal_pert.append(TidalEffects(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp24_tidal_effects.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp24_tidal_pert.append(TidalEffects(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp25_tidal_effects.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp25_tidal_pert.append(TidalEffects(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp26_tidal_effects.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp26_tidal_pert.append(TidalEffects(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp27_tidal_effects.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp27_tidal_pert.append(TidalEffects(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp28_moon_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp28_moon_pert.append(MoonPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp29_moon_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp29_moon_pert.append(MoonPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp30_moon_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp30_moon_pert.append(MoonPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp31_rel_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp31_rel_pert.append(RelPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp32_rel_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp32_rel_pert.append(RelPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp33_rel_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp33_rel_pert.append(RelPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp34_sol_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp34_sol_pert.append(SolPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp35_sol_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp35_sol_pert.append(SolPart(line))
    file.close()
    file = open('novapy/solar_system/lunar/elp36_sol_pert.data', 'r')
    file_lines = file.readlines()
    for line in file_lines:
        elp36_sol_pert.append(SolPart(line))
    file.close()
    '''
    print('elp1 = ', len(elp1_main))
    print('elp2 = ', len(elp2_main))
    print('elp3 = ', len(elp3_main))
    print('elp4 = ', len(elp4_earth_pert))
    print('elp5 = ', len(elp5_earth_pert))
    print('[elp6] = ', len(elp6_earth_pert))
    print('[elp7] = ', len(elp7_earth_pert))
    print('[elp8] = ', len(elp8_earth_pert))
    print('[elp9] = ', len(elp9_earth_pert))
    print('[elp10] = ', len(elp10_planet_pert))
    print('[elp11] = ', len(elp11_planet_pert))
    print('[elp12] = ', len(elp12_planet_pert))
    print('[elp13] = ', len(elp13_planet_pert))
    print('[elp14] = ', len(elp14_planet_pert))
    print('[elp15] = ', len(elp15_planet_pert))
    print('[elp16] = ', len(elp16_planet_pert))
    print('[elp17] = ', len(elp17_planet_pert))
    print('[elp18] = ', len(elp18_planet_pert))
    print('[elp19] = ', len(elp19_planet_pert))
    print('[elp20] = ', len(elp20_planet_pert))
    print('[elp21] = ', len(elp21_planet_pert))
    print('[elp22] = ', len(elp22_tidal_pert))
    print('[elp23] = ', len(elp23_tidal_pert))
    print('[elp24] = ', len(elp24_tidal_pert))
    print('[elp25] = ', len(elp25_tidal_pert))
    print('[elp26] = ', len(elp26_tidal_pert))
    print('[elp27] = ', len(elp27_tidal_pert))
    print('[elp28] = ', len(elp28_moon_pert))
    print('[elp29] = ', len(elp29_moon_pert))
    print('[elp30] = ', len(elp30_moon_pert))
    print('[elp31] = ', len(elp31_rel_pert))
    print('[elp32] = ', len(elp32_rel_pert))
    print('[elp33] = ', len(elp33_rel_pert))
    print('[elp34] = ', len(elp34_sol_pert))
    print('[elp35] = ', len(elp35_sol_pert))
    print('[elp36] = ', len(elp36_sol_pert))
    '''


def sum_series_elp1(t):
    result, y = 0, 0
    for elp in elp1_main:
        # derivatives of a
        tgv = elp.b[0] + DTASM * elp.b[4]
        x = elp.a + tgv * (DELNP - AM * DELNU) + elp.b[1] * DELG + elp.b[2] * DELE + elp.b[3] * DELEP
        for k in range(5):
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += x * sin(y)
    return result

def sum_series_elp2(t):
    result, y = 0, 0
    for elp in elp2_main:
        # derivatives of a
        tgv = elp.b[0] + DTASM * elp.b[4]
        x = elp.a + tgv * (DELNP - AM * DELNU) + elp.b[1] * DELG + elp.b[2] * DELE + elp.b[3] * DELEP
        for k in range(5):
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += x * sin(y)
    return result

def sum_series_elp3(t):
    result, y = 0, 0
    for elp in elp3_main:
        # derivatives of a
        tgv = elp.b[0] + DTASM * elp.b[4]
        x = elp.a + tgv * (DELNP - AM * DELNU) + elp.b[1] * DELG + elp.b[2] * DELE + elp.b[3] * DELEP
        for k in range(5):
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y += M_PI_2
        y = ln_range_radians2(y)
        result += x * sin(y)
    return result
def sum_series_elp4(t):
    result, y = 0, 0
    for elp in elp4_earth_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result
def sum_series_elp5(t):
    result, y = 0, 0
    for elp in elp5_earth_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp6(t):
    result, y = 0, 0
    for elp in elp6_earth_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp7(t):
    result, y = 0, 0
    for elp in elp7_earth_pert:
        a = elp.a * t[1]
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += a * sin(y)
    return result


def sum_series_elp8(t):
    result, y = 0, 0
    for elp in elp8_earth_pert:
        a = elp.a * t[1]
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += a * sin(y)
    return result


def sum_series_elp9(t):
    result, y = 0, 0
    for elp in elp9_earth_pert:
            a = elp.a * t[1]
            y = elp.o * DEG
            for k in range(2):
                y += elp.iz * zeta[k] * t[k]
                for i in range(4):
                    y += elp.ilu[i] * delt[i][k] * t[k]
            y = ln_range_radians2(y)
            result += a * sin(y)
    return result

def sum_series_elp10(t):
    result = 0
    for elp in elp10_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            y += (elp.ipla[8] * delt[0][k] + elp.ipla[9] * delt[2][k] + elp.ipla[10] * delt[3][k]) * t[k]
            for i in range(8):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.o * sin(y)
    return result


def sum_series_elp11(t):
    result = 0
    for elp in elp11_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            y += (elp.ipla[8] * delt[0][k] + elp.ipla[9] * delt[2][k] + elp.ipla[10] * delt[3][k]) * t[k]
            for i in range(8):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.o * sin(y)
    return result


def sum_series_elp12(t):
    result = 0
    for elp in elp12_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            y += (elp.ipla[8] * delt[0][k] + elp.ipla[9] * delt[2][k] + elp.ipla[10] * delt[3][k]) * t[k]
            for i in range(8):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.o * sin(y)
    return result
def sum_series_elp13(t):
    result = 0
    for elp in elp13_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            y += (elp.ipla[8] * delt[0][k] + elp.ipla[9] * delt[2][k] + elp.ipla[10] * delt[3][k]) * t[k]
            for i in range(8):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        x = elp.o * t[1]
        result += x * sin(y)
    return result
def sum_series_elp14(t):
    result = 0
    for elp in elp14_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            y += (elp.ipla[8] * delt[0][k] + elp.ipla[9] * delt[2][k] + elp.ipla[10] * delt[3][k]) * t[k]
            for i in range(8):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        x = elp.o * t[1]
        result += x * sin(y)
    return result
def sum_series_elp15(t):
    result = 0
    for elp in elp15_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            y += (elp.ipla[8] * delt[0][k] + elp.ipla[9] * delt[2][k] + elp.ipla[10] * delt[3][k]) * t[k]
            for i in range(8):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        x = elp.o * t[1]
        result += x * sin(y)
    return result


def sum_series_elp16(t):
    result = 0
    for elp in elp16_planet_pert:

        y = elp.theta * DEG
        for k in range(2):
            for i in range(4):
                y += elp.ipla[i+7] * delt[i][k] * t[k]
            for i in range(7):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.o * sin(y)
    return result


def sum_series_elp17(t):
    result = 0
    for elp in elp17_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            for i in range(4):
                y += elp.ipla[i+7] * delt[i][k] * t[k]
            for i in range(7):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.o * sin(y)
    return result
def sum_series_elp18(t):
    result = 0
    for elp in elp18_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            for i in range(4):
                y += elp.ipla[i+7] * delt[i][k] * t[k]
            for i in range(7):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.o * sin(y)
    return result
def sum_series_elp19(t):
    result = 0
    for elp in elp19_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            for i in range(4):
                y += elp.ipla[i+7] * delt[i][k] * t[k]
            for i in range(7):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        x = elp.o * t[1]
        result += x * sin(y)
    return result


def sum_series_elp20(t):
    result = 0
    for elp in elp20_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            for i in range(4):
                y += elp.ipla[i+7] * delt[i][k] * t[k]
            for i in range(7):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        x = elp.o * t[1]
        result += x * sin(y)
    return result


def sum_series_elp21(t):
    result = 0
    for elp in elp21_planet_pert:
        y = elp.theta * DEG
        for k in range(2):
            for i in range(4):
                y += elp.ipla[i+7] * delt[i][k] * t[k]
            for i in range(7):
                y += elp.ipla[i] * p[i][k] * t[k]
        y = ln_range_radians2(y)
        x = elp.o * t[1]
        result += x * sin(y)
    return result


def sum_series_elp22(t):
    result = 0
    for elp in elp22_tidal_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp23(t):
    result = 0
    for elp in elp23_tidal_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp24(t):
    result = 0
    for elp in elp24_tidal_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp25(t):
    result = 0
    for elp in elp25_tidal_pert:
        a = elp.a * t[1]
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += a * sin(y)
    return result


def sum_series_elp26(t):
    result = 0
    for elp in elp26_tidal_pert:
        a = elp.a * t[1]
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += a * sin(y)
    return result


def sum_series_elp27(t):
    result = 0
    for elp in elp27_tidal_pert:
        a = elp.a * t[1]
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += a * sin(y)
    return result


def sum_series_elp28(t):
    result = 0
    for elp in elp28_moon_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp29(t):
    result = 0
    for elp in elp29_moon_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):

                y += elp.ilu[i] * delt[i][k] * t[k]

        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp30(t):
    result = 0
    for elp in elp30_moon_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result

def sum_series_elp31(t):
    result = 0
    for elp in elp31_rel_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp32(t):
    result = 0
    for elp in elp32_rel_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp33(t):
    result = 0
    for elp in elp33_rel_pert:
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += elp.a * sin(y)
    return result


def sum_series_elp34(t):
    result = 0
    for elp in elp34_sol_pert:
        a = elp.a * t[2]
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += a * sin(y)
    return result


def sum_series_elp35(t):
    result = 0
    for elp in elp35_sol_pert:
        a = elp.a * t[2]
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += a * sin(y)
    return result


def sum_series_elp36(t):
    result = 0.
    for elp in elp36_sol_pert:
        a = elp.a * t[2]
        y = elp.o * DEG
        for k in range(2):
            y += elp.iz * zeta[k] * t[k]
            for i in range(4):
                y += elp.ilu[i] * delt[i][k] * t[k]
        y = ln_range_radians2(y)
        result += a * sin(y)
    return result


load_data()
def ln_get_lunar_geo_posn(jd, rect_posn, precision):
    if precision > 0.01:
        precision = 0.01
    jd_c = (jd - 2451545.0) / 36525.
    t = [1.0]
    t.append(jd_c)
    t.append(t[1]*t[1])
    t.append(t[2]*t[1])
    t.append(t[3]*t[1])

    pre = [precision * RAD, precision * RAD, precision * ATH]

    elp = [
        sum_series_elp1(t),
        sum_series_elp2(t),
        sum_series_elp3(t),
        sum_series_elp4(t),
        sum_series_elp5(t),
        sum_series_elp6(t),
        sum_series_elp7(t),
        sum_series_elp8(t),
        sum_series_elp9(t),
        sum_series_elp10(t),
        sum_series_elp11(t),
        sum_series_elp12(t),
        sum_series_elp13(t),
        sum_series_elp14(t),
        sum_series_elp15(t),
        sum_series_elp16(t),
        sum_series_elp17(t),
        sum_series_elp18(t),
        sum_series_elp19(t),
        sum_series_elp20(t),
        sum_series_elp21(t),
        sum_series_elp22(t),
        sum_series_elp23(t),
        sum_series_elp24(t),
        sum_series_elp25(t),
        sum_series_elp26(t),
        sum_series_elp27(t),
        sum_series_elp28(t),
        sum_series_elp29(t),
        sum_series_elp30(t),
        sum_series_elp31(t),
        sum_series_elp32(t),
        sum_series_elp33(t),
        sum_series_elp34(t),
        sum_series_elp35(t),
        sum_series_elp36(t)]

    a = elp[0] + elp[3] + elp[6] + elp[9] + elp[12] + elp[15] + elp[18] + \
        elp[21] + elp[24] + elp[27] + elp[30] + elp[33]
    b = elp[1] + elp[4] + elp[7] + elp[10] + elp[13] + elp[16] + elp[19] + \
        elp[22] + elp[25] + elp[28] + elp[31] + elp[34]
    c = elp[2] + elp[5] + elp[8] + elp[11] + elp[14] + elp[17] + elp[20] + \
        elp[23] + elp[26] + elp[29] + elp[32] + elp[35]
    # calculate geocentric coords
    a = a / RAD + W1[0] + (W1[1] * t[1]) + (W1[2] * t[2]) + (W1[3] * t[3]) + (W1[4] * t[4])
    b = b / RAD
    c = c * A0 / ATH

    x = c * cos(b)
    y = x * sin(a)
    x = x * cos(a)
    z = c * sin(b)

    # Laskars series
    pw = (P1 + P2 * t[1] + P3 * t[2] + P4 * t[3] + P5 * t[4]) * t[1]
    qw = (Q1 + Q2 * t[1] + Q3 * t[2] + Q4 * t[3] + Q5 * t[4]) * t[1]
    ra = 2.0 * sqrt(1 - pw * pw - qw * qw)
    pwqw = 2.0 * pw * qw
    pw2 = 1.0 - 2.0 * pw * pw
    qw2 = 1.0 - 2.0 * qw * qw
    pw = pw * ra
    qw = qw * ra
    a = pw2 * x + pwqw * y + pw * z
    b = pwqw * x + qw2 * y - qw * z
    c = -pw * x + qw * y + (pw2 + qw2 - 1) * z

    rect_posn.x = a
    rect_posn.y = b
    rect_posn.z = c

def ln_get_lunar_equ_coords_prec(jd, equ_pos, precision):
    ecl = LnLnlatPosn()
    ln_get_lunar_ecl_coords(jd, ecl, precision)
    ln_get_equ_from_ecl(ecl, jd, equ_pos)


def ln_get_lunar_equ_coords(jd, equ_pos):
    ln_get_lunar_equ_coords_prec(jd, equ_pos, 0)


def ln_get_lunar_ecl_coords(jd, lnlat_pos, precision):
    moon = LnRectPosn()
    ln_get_lunar_geo_posn(jd, moon, precision)
    lnlat_pos.lng = atan2(moon.y, moon.x)
    lnlat_pos.lat = atan2(moon.z, (sqrt((moon.x * moon.x) + (moon.y * moon.y))))
    lnlat_pos.lng = ln_range_degrees(ln_rad_to_deg(lnlat_pos.lng))
    lnlat_pos.lat = ln_rad_to_deg(lnlat_pos.lat)



def ln_get_lunar_earth_dist(jd):
    moon = LnRectPosn()
    ln_get_lunar_geo_posn(jd, moon, 0.00001)
    return sqrt((moon.x * moon.x) + (moon.y * moon.y) + (moon.z * moon.z))




def ln_get_lunar_phase(jd):
    moon = LnLnlatPosn()
    sunlp = LnLnlatPosn()
    ln_get_lunar_ecl_coords(jd, moon, 0.0001)
    ln_get_solar_ecl_coords(jd, sunlp)
    lunar_elong = acos(cos(ln_deg_to_rad(moon.lat)) * cos(ln_deg_to_rad(sunlp.lng - sunlp.lng)))
    r = ln_get_earth_solar_dist(jd)
    delta = ln_get_lunar_earth_dist(jd)
    r = r * AU
    phase = atan2((r * sin(lunar_elong)), (delta - r * cos(lunar_elong)))
    return ln_rad_to_deg(phase)


def ln_get_lunar_disk(jd):
    i = ln_deg_to_rad(ln_get_lunar_phase(jd))
    return (1.0 + cos(i)) / 2.0


def ln_get_lunar_bright_limb(jd):
    moon = LnEquPosn()
    sunlp = LnEquPosn()
    ln_get_lunar_equ_coords(jd, moon)
    ln_get_solar_equ_coords(jd, sunlp)
    x = cos(ln_deg_to_rad(sunlp.dec)) * sin(ln_deg_to_rad(sunlp.ra - moon.ra))
    y = sin((ln_deg_to_rad(sunlp.dec)) * cos(ln_deg_to_rad(moon.dec))) - \
        (cos(ln_deg_to_rad(sunlp.dec)) * sin(ln_deg_to_rad(moon.dec)) * cos(ln_deg_to_rad(sunlp.ra - moon.ra)))
    angle = atan2(x, y)
    angle = ln_range_radians(angle)
    return ln_rad_to_deg(angle)


def ln_get_lunar_rst(jd, obs, rst):
    body_coords = IGetEquBodyCoords()
    body_coords.name('lunar')
    return ln_get_body_rst_horizon(jd, obs, body_coords, LN_LUNAR_STANDARD_HORIZON, rst)


def ln_get_lunar_sdiam(jd):
    So = 358473400
    dist = ln_get_lunar_earth_dist(jd)
    return So / dist


def ln_get_lunar_long_asc_node(jd):
    T = (jd - 2451545.0) / 36525.0
    omega = 125.0445479
    T2 = T * T
    T3 = T2 * T
    T4 = T3 * T
    omega -= 1934.1362891 * T + 0.0020754 * T2 + T3 / 467441.0 - T4 / 60616000.0
    return omega


def ln_get_lunar_long_perigee(jd):
    T = (jd - 2451545.0) / 36525.0
    per = 83.3532465
    T2 = T * T
    T3 = T2 * T
    T4 = T3 * T
    per += 4069.0137287 * T - 0.0103200 * T2 - T3 / 80053.0 + T4 / 18999000.0
    return per




from novapy.util.i_get_equ_body_coords import IGetEquBodyCoords
