

class LnZoneDate:
    years = int()
    months = int()
    days = int()
    hours = int()
    minutes = int()
    seconds = float()

    #  Timezone offset. Seconds east of UTC. Valid values 0..86400
    gmtoff = int()


    def ch_0(self, num):
        if num < 10:
            return '0'
        else:
            return ''

    def get_string(self):

        string = '{0}{1}/'.format(self.ch_0(self.months), self.months)
        string += '{0}{1}/'.format(self.ch_0(self.days), self.days)
        string += str(self.years)

        string += '  {0}{1}:'.format(self.ch_0(self.hours), self.hours)
        string += '{0}{1}:'.format(self.ch_0(self.minutes), self.minutes)
        string += '{0}{1}'.format(self.ch_0(self.seconds), int(self.seconds))
        string += ' {0}'.format(self.gmtoff / 3600)

        return string
