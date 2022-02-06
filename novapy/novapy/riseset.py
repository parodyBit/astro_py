from novapy.sidereal_time import ln_get_apparent_sidereal_time

from novapy.utility import nan
from novapy.utility import ln_deg_to_rad
from novapy.utility import ln_rad_to_deg
from novapy.utility import ln_range_degrees
from novapy.utility import ln_interpolate3


from novapy.api.ln_rst_time import LnRstTime
from novapy.api.ln_equ_posn import LnEquPosn
from novapy.dynamical_time import ln_get_jde
from novapy.dynamical_time import ln_get_dynamical_time_diff


from math import cos
from math import sin
from math import acos


LN_STAR_STANDARD_HORIZON = -0.5667


def check_coords(obs, h1, horizon, obj):
    # helper function to check if object can be visible
    # check if body is circumpolar
    if abs(h1) > 1.0:
        # check if maximal height < horizon
        h = 90 + obj.dec - obs.lat
        if h > 90.0:
            h = 180.0 - h
        if h < -90:
            h = -180.0 - h
        if h < horizon:
            return -1
        return 1
    return 0


def ln_get_object_rst(jd, obs, obj, rst):
    return ln_get_object_rst_horizon(jd, obs, obj, LN_STAR_STANDARD_HORIZON, rst)


def ln_get_object_rst_horizon(jd, obs, obj, horizon, rst):
    # this functions returns 1 if the object is circumpolar, that is it
    # remains the whole day above the horizon. Returns -1 when it remains whole
    # day bellow the horizon.
    return ln_get_object_rst_horizon_offset(jd, obs, obj, horizon, rst, 0.5)


def set_next_rst(rst, diff, out):
    out.rise = rst.rise + diff
    out.transit = rst.transit + diff
    out.set = rst.set + diff


def find_next(jd, jd1, jd2, jd3):
    if jd and jd1 is None:
        return jd3
    if jd < jd1:
        return jd1
    if jd < jd2:
        return jd2
    return jd3


def ln_get_object_next_rst(jd, obs, obj, rst):
    return ln_get_object_next_rst_horizon(jd, obs, obj, LN_STAR_STANDARD_HORIZON, rst)


def ln_get_object_rst_horizon_offset(jd, obs, obj, horizon, rst, ut_offset):
    if ut_offset is None:
        jd_ut = jd
    else:
        jd_ut = jd + ut_offset

    o = ln_get_apparent_sidereal_time(jd_ut)
    o *= 15.0

    h0 = (sin(ln_deg_to_rad(horizon))) - sin(ln_deg_to_rad(obs.lat) * sin(ln_deg_to_rad(obj.dec)))
    h1 = (cos(ln_deg_to_rad(obs.lat)) * cos(ln_deg_to_rad(obj.dec)))

    h1 = h0 / h1

    ret = check_coords(obs, h1, horizon, obj)
    if ret != 0:
        return ret

    h0 = acos(h1)
    h0 = ln_rad_to_deg(h0)

    mt = (obj.ra - obs.lng - o) / 360.0
    mr = mt - h0 / 360.0
    ms = mt + h0 / 360.0

    for m in range(3):
        if mt > 1.0:
            mt -= 1
        elif mt < 0:
            mt += 1
        if mr > 1.0:
            mr -= 1
        elif mr < 0:
            mr += 1
        if ms > 1.0:
            ms -= 1
        elif ms < 0:
            ms += 1
        # find sidereal time at Greenwich, in degrees, for each m
        mst = o + 360.985647 * mt
        msr = o + 360.985647 * mr
        mss = o + 360.985647 * ms

        # find local hour angle
        hat = mst + obs.lng - obj.ra
        har = msr + obs.lng - obj.ra
        has = mss + obs.lng - obj.ra

        # find altitude for rise and set
        altr = sin(ln_deg_to_rad(obs.lat)) \
            * sin(ln_deg_to_rad(obj.dec)) \
            + cos(ln_deg_to_rad(obs.lat)) \
            * cos(ln_deg_to_rad(obj.dec)) * cos(ln_deg_to_rad(har))
        alts = sin(ln_deg_to_rad(obs.lat)) \
            * sin(ln_deg_to_rad(obj.dec)) \
            + cos(ln_deg_to_rad(obs.lat)) \
            * cos(ln_deg_to_rad(obj.dec)) * cos(ln_deg_to_rad(has))

        altr = ln_rad_to_deg(altr)
        alts = ln_rad_to_deg(alts)

        # corrections for m
        ln_range_degrees(hat)
        if hat > 180.0:
            hat -= 360

        dmt = -(hat / 360.0)
        dmr = (altr - horizon) / (360 * cos(ln_deg_to_rad(obj.dec)) *
                                  cos(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(har)))
        dms = (alts - horizon) / (360 * cos(ln_deg_to_rad(obj.dec)) *
                                  cos(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(has)))

        # add corrections and change to JD
        mt += dmt
        mr += dmr
        ms += dms
        if 0.0 <= mt <= 1.0 and 0.0 <= mr <= 1.0 and 0.0 <= ms <= 1.0:
            break
    rst.rise = jd_ut + mr
    rst.transit = jd_ut + mt
    rst.set = jd_ut + ms

    # not circumpolar
    return 0


def ln_get_object_next_rst_horizon(jd, obs, obj, horizon, rst):
    rst_1 = LnRstTime()
    rst_2 = LnRstTime()

    ret = ln_get_object_rst_horizon_offset(jd, obs, obj, horizon, rst, nan('0'))
    if ret != 0:
        return ret

    if rst.rise > (jd + 0.5) or rst.transit > (jd + 0.5) or rst.set > (jd + 0.5):
        ln_get_object_rst_horizon_offset(jd-1, obs, obj, horizon, rst_1, nan('0'))
    else:
        set_next_rst(rst, 1.0, rst_2)
    rst.rise = find_next(jd, rst_1.rise, rst.rise, rst_2.rise)
    rst.transit = find_next(jd, rst_1.transit, rst.transit, rst_2.transit)
    rst.set = find_next(jd, rst_1.set, rst.set, rst_2.set)

    if rst.rise is None:
        return ret
    return 0


def ln_get_body_rst_horizon(jd, obs, get_equ_body_coords, horizon, rst):
    return ln_get_body_rst_horizon_offset(jd, obs, get_equ_body_coords, horizon, rst, 0.5)


def ln_get_body_rst_horizon_offset(jd, obs, get_equ_body_coords, horizon, rst, ut_offset):
    sol1 = LnEquPosn()
    sol2 = LnEquPosn()
    sol3 = LnEquPosn()
    post = LnEquPosn()
    posr = LnEquPosn()
    poss = LnEquPosn()

    t = ln_get_dynamical_time_diff(jd)
    jd_ut = 0.0
    if ut_offset is None:
        jd_ut = jd
    else:
        jd_ut = jd + ut_offset

    jd_ut = jd
    o = ln_get_apparent_sidereal_time(jd_ut)
    o *= 15.0

    get_equ_body_coords.get_equ_body_coords(jd_ut - 1.0, sol1)
    get_equ_body_coords.get_equ_body_coords(jd_ut, sol2)
    get_equ_body_coords.get_equ_body_coords(jd_ut + 1.0, sol3)

    h0 = (sin(ln_deg_to_rad(horizon))) - sin(ln_deg_to_rad(obs.lat) * sin(ln_deg_to_rad(sol2.dec)))
    h1 = (cos(ln_deg_to_rad(obs.lat)) * cos(ln_deg_to_rad(sol2.dec)))

    h1 = h0 / h1

    ret = check_coords(obs, h1, horizon, sol2)
    if ret != 0:
        return ret

    h0 = acos(h1)
    h0 = ln_rad_to_deg(h0)

    if (sol1.ra - sol2.ra) > 180.0:
        sol2.ra += 360.0
    if (sol2.ra - sol3.ra) > 180.0:
        sol3.ra += 360.0
    if (sol3.ra - sol2.ra) > 180.0:
        sol3.ra -= 360.0
    if (sol2.ra - sol1.ra) > 180.0:
        sol3.ra -= 360.0

    mt = (sol2.ra - obs.lng - o) / 360.0
    mr = mt - h0 / 360.0
    ms = mt + h0 / 360.0

    for m in range(3):
        if mt > 1.0:
            mt -= 1
        elif mt < 0:
            mt += 1
        if mr > 1.0:
            mr -= 1
        elif mr < 0:
            mr += 1
        if ms > 1.0:
            ms -= 1
        elif ms < 0:
            ms += 1
        # find sidereal time at Greenwich, in degrees, for each m
        mst = o + 360.985647 * mt
        msr = o + 360.985647 * mr
        mss = o + 360.985647 * ms

        nt = mt + t / 86400.0
        nr = mr + t / 86400.0
        ns = ms + t / 86400.0

        # interpolate ra and dec for each m, except for transit dec (dec2)
        posr.ra = ln_interpolate3(nr, sol1.ra, sol2.ra, sol3.ra)
        posr.dec = ln_interpolate3(nr, sol1.dec, sol2.dec, sol3.dec)
        post.ra = ln_interpolate3(nt, sol1.ra, sol2.ra, sol3.ra)
        poss.ra = ln_interpolate3(ns, sol1.ra, sol2.ra, sol3.ra)
        poss.dec = ln_interpolate3(ns, sol1.dec, sol2.dec, sol3.dec)

        hat = mst + obs.lng - post.ra
        har = msr + obs.lng - posr.ra
        has = mss + obs.lng - poss.ra

        # find altitude for rise and set
        altr = sin(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(posr.dec)) + cos(ln_deg_to_rad(obs.lat)) * \
            cos(ln_deg_to_rad(posr.dec)) * cos(ln_deg_to_rad(har))
        alts = sin(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(poss.dec)) + cos(ln_deg_to_rad(obs.lat)) * \
            cos(ln_deg_to_rad(poss.dec)) * cos(ln_deg_to_rad(has))

        altr = ln_rad_to_deg(altr)
        alts = ln_rad_to_deg(alts)

        # corrections for m
        ln_range_degrees(hat)
        if hat > 180.0:
            hat -= 360

        dmt = -(hat / 360.0)
        dmr = (altr - horizon) / (360 * cos(ln_deg_to_rad(posr.dec))
                                  * cos(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(har)))
        dms = (alts - horizon) / (360 * cos(ln_deg_to_rad(poss.dec))
                                  * cos(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(has)))

        # add corrections and change to JD
        mt += dmt
        mr += dmr
        ms += dms
        if 0.0 <= mt <= 1.0 and 0.0 <= mr <= 1.0 and 0.0 <= ms <= 1.0:
            break
    rst.rise = jd_ut + mr
    rst.transit = jd_ut + mt
    rst.set = jd_ut + ms

    # not circumpolar
    return 0


def ln_get_body_next_rst_horizon(jd, obs, get_equ_body_coords, horizon, rst):
    return ln_get_body_next_rst_horizon_future(jd, obs, get_equ_body_coords, horizon, 1, rst)


def ln_get_body_next_rst_horizon_future(jd, obs, get_equ_body_coords, horizon, daily_limit, rst):
    rst_1 = LnRstTime()
    rst_2 = LnRstTime()
    ret = ln_get_body_rst_horizon_offset(jd, obs, get_equ_body_coords, horizon, rst, nan('0'))

    if ret != 0 and daily_limit == 1:
        # circumpolar
        return ret

    if ret == 0 and (rst.rise > (jd + 0.5) or rst.transit > (jd + 0.5) or rst.set > (jd + 0.5)):
        ret = ln_get_body_rst_horizon_offset(jd - 1, obs, get_equ_body_coords, horizon, rst_1, nan('0'))
    if ret != 0:
        set_next_rst(rst, -1, rst_1)
    else:
        rst.rise = nan('0')
        rst.transit = nan('0')
        rst.set = nan('0')
        set_next_rst(rst, -1, rst_1)
    if ret != 0 or (rst.rise < jd or rst.transit < jd or rst.set < jd):
        day = 1

        while day <= daily_limit:
            ret = ln_get_body_rst_horizon_offset(jd + day, obs, get_equ_body_coords, horizon, rst_2, nan('0'))
            if ret == 0:
                day = daily_limit + 2
                break
            day += 1
        if day == daily_limit + 1:
            return ret
    else:
        set_next_rst(rst, +1, rst_2)
    rst.rise = find_next(jd, rst_1.rise, rst.rise, rst_2.rise)
    rst.transit = find_next(jd, rst_1.transit, rst.transit, rst_2.transit)
    rst. set = find_next(jd, rst_1.set, rst.set, rst_2.set)
    if rst.rise is None:
        return ret
    return 0


def ln_get_motion_body_rst_horizon_offset(jd, obs, get_motion_body_coords, orbit, horizon, rst, ut_offset):
    sol1 = LnEquPosn()
    sol2 = LnEquPosn()
    sol3 = LnEquPosn()
    post = LnEquPosn()
    posr = LnEquPosn()
    poss = LnEquPosn()

    t = ln_get_dynamical_time_diff(jd)

    if ut_offset is None:
        jd_ut = jd
    else:
        jd_ut = jd + ut_offset

    jd_ut = jd
    o = ln_get_apparent_sidereal_time(jd_ut)
    o *= 15.0
    get_motion_body_coords.get_motion_body_coords(jd_ut - 1.0, orbit, sol1)
    get_motion_body_coords.get_motion_body_coords(jd_ut, orbit, sol2)
    get_motion_body_coords.get_motion_body_coords(jd_ut + 1.0, orbit, sol3)

    h0 = (sin(ln_deg_to_rad(horizon))) - sin(ln_deg_to_rad(obs.lat) * sin(ln_deg_to_rad(sol2.dec)))
    h1 = (cos(ln_deg_to_rad(obs.lat)) * cos(ln_deg_to_rad(sol2.dec)))

    h1 = h0 / h1

    ret = check_coords(obs, h1, horizon, sol2)
    if ret != 0:
        return ret

    h0 = acos(h1)
    h0 = ln_rad_to_deg(h0)

    if (sol1.ra - sol2.ra) > 180.0:
        sol2.ra += 360.0
    if (sol2.ra - sol3.ra) > 180.0:
        sol3.ra += 360.0
    if (sol3.ra - sol2.ra) > 180.0:
        sol3.ra -= 360.0
    if (sol2.ra - sol1.ra) > 180.0:
        sol3.ra -= 360.0

    mt = (sol2.ra - obs.lng - o) / 360.0
    mr = mt - h0 / 360.0
    ms = mt + h0 / 360.0

    for m in range(3):
        if mt > 1.0:
            mt -= 1
        elif mt < 0:
            mt += 1
        if mr > 1.0:
            mr -= 1
        elif mr < 0:
            mr += 1
        if ms > 1.0:
            ms -= 1
        elif ms < 0:
            ms += 1
        # find sidereal time at Greenwich, in degrees, for each m
        mst = o + 360.985647 * mt
        msr = o + 360.985647 * mr
        mss = o + 360.985647 * ms

        nt = mt + t / 86400.0
        nr = mr + t / 86400.0
        ns = ms + t / 86400.0

        # interpolate ra and dec for each m, except for transit dec (dec2)
        posr.ra = ln_interpolate3(nr, sol1.ra, sol2.ra, sol3.ra)
        posr.dec = ln_interpolate3(nr, sol1.dec, sol2.dec, sol3.dec)
        post.ra = ln_interpolate3(nt, sol1.ra, sol2.ra, sol3.ra)
        poss.ra = ln_interpolate3(ns, sol1.ra, sol2.ra, sol3.ra)
        poss.dec = ln_interpolate3(ns, sol1.dec, sol2.dec, sol3.dec)

        hat = mst + obs.lng - post.ra
        har = msr + obs.lng - posr.ra
        has = mss + obs.lng - poss.ra

        # find altitude for rise and set
        altr = sin(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(posr.dec)) + cos(ln_deg_to_rad(obs.lat)) * \
            cos(ln_deg_to_rad(posr.dec)) * cos(ln_deg_to_rad(har))
        alts = sin(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(poss.dec)) + cos(ln_deg_to_rad(obs.lat)) * \
            cos(ln_deg_to_rad(poss.dec)) * cos(ln_deg_to_rad(has))

        altr = ln_rad_to_deg(altr)
        alts = ln_rad_to_deg(alts)

        # corrections for m
        ln_range_degrees(hat)
        if hat > 180.0:
            hat -= 360

        dmt = -(hat / 360.0)
        dmr = (altr - horizon) / (360 * cos(ln_deg_to_rad(posr.dec))
                                  * cos(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(har)))
        dms = (alts - horizon) / (360 * cos(ln_deg_to_rad(poss.dec))
                                  * cos(ln_deg_to_rad(obs.lat)) * sin(ln_deg_to_rad(has)))

        # add corrections and change to JD
        mt += dmt
        mr += dmr
        ms += dms
        if 0.0 <= mt <= 1.0 and 0.0 <= mr <= 1.0 and 0.0 <= ms <= 1.0:
            break
    rst.rise = jd_ut + mr
    rst.transit = jd_ut + mt
    rst.set = jd_ut + ms

    # not circumpolar
    return 0


def ln_get_motion_body_next_rst_horizon(jd, obs, get_motion_body_coords, orbit, horizon, rst):
    return ln_get_motion_body_next_rst_horizon_future(jd, obs, get_motion_body_coords, orbit, horizon, 1, rst)


def ln_get_motion_body_next_rst_horizon_future(jd, obs, get_motion_body_coords, orbit, horizon, daily_limit, rst):
    rst_1 = LnRstTime()
    rst_2 = LnRstTime()
    ret = ln_get_motion_body_rst_horizon_offset(jd, obs, get_motion_body_coords, orbit, horizon, rst, nan('0'))

    if ret != 0 and daily_limit == 1:
        # circumpolar
        return ret

    if ret == 0 and (rst.rise > (jd + 0.5) or rst.transit > (jd + 0.5) or rst.set > (jd + 0.5)):
        ret = ln_get_motion_body_rst_horizon_offset(
            jd - 1, obs, get_motion_body_coords, orbit, horizon, rst_1, nan('0'))
    if ret != 0:
        set_next_rst(rst, -1, rst_1)
    else:
        rst.rise = nan('0')
        rst.transit = nan('0')
        rst.set = nan('0')
        set_next_rst(rst, -1, rst_1)
    if ret != 0 or (rst.rise < jd or rst.transit < jd or rst.set < jd):
        day = 1

        while day <= daily_limit:
            ret = ln_get_motion_body_rst_horizon_offset(
                jd + day, obs, get_motion_body_coords, orbit, horizon, rst_2, nan('0'))
            if ret == 0:
                day = daily_limit + 2
                break
            day += 1
        if day == daily_limit + 1:
            return ret
    else:
        set_next_rst(rst, +1, rst_2)
    rst.rise = find_next(jd, rst_1.rise, rst.rise, rst_2.rise)
    rst.transit = find_next(jd, rst_1.transit, rst.transit, rst_2.transit)
    rst.set = find_next(jd, rst_1.set, rst.set, rst_2.set)
    if rst.rise is None:
        return ret
    return 0


def ln_get_motion_body_rst_horizon(jd, obs, motion_body_coords, orbit, horizon, rst):
    return ln_get_motion_body_rst_horizon_offset(jd, obs, motion_body_coords, orbit, horizon, rst, 0.5)
