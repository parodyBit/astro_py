import json

class TimeZoneHandler:
    time_zones = {}
    __instance = None

    @staticmethod
    def getMaster():
        if TimeZoneHandler.__instance == None:
            TimeZoneHandler()
        return TimeZoneHandler.__instance

    def __init__(self):
        if TimeZoneHandler.__instance == None:
            TimeZoneHandler.__instance = self
            self.__load_data()
        else:
            print('singleton')

    def __load_data(self):
        with open("novapy/timezones.json", "r") as read_file:
            data = json.load(read_file)
            for item in data:
                # print(item)
                tz = TimeZone()
                tz.name = item['value']
                tz.abbr = item['abbr']
                tz.offset = item['offset']
                tz.isdst = item['isdst']
                tz.text = item['text']
                tz.utc = item['utc']
                self.add_time_zone(tz)
        # print('total added', len(self.time_zones))

    def add_time_zone(self, time_zone):
        self.time_zones[time_zone.name] = time_zone


class TimeZone:
    name = ''
    abbr = ''
    offset = int()
    isdst = bool()
    text = ''
    utc = []

    def __init__(self): pass

