from dataclasses import dataclass


@dataclass
class LnDate:
    def __init__(self):
        pass

    years: int
    months: int
    days: int
    hours: int
    minutes: int
    seconds: float
    millis: float

    def __copy__(self):
        date = LnDate()
        date.years = self.years
        date.months = self.months
        date.days = self.days
        date.minutes = self.minutes
        date.seconds = self.seconds
        return date

    def copy(self, date):
        self.years = date.years
        self.months = date.months
        self.days = date.days
        self.hours = date.hours
        self.minutes = date.minutes
        self.seconds = date.seconds

    def print_debug(self):
        print(self.get_string())


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

        return string

