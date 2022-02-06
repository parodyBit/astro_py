
class LnLnlatPosn:

    #  Longitude. Object longitude
    lng = float()

    #  Latitude. Object latitude
    lat = float()

    def set_position(self, longitude, latitude):
        self.lng = longitude
        self.lat = latitude

    def print_position(self):
        print('{0} {1}'.format(self.lng, self.lat))
