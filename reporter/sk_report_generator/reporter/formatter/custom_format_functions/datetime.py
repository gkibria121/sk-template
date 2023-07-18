from ..base import IFormatter
import datetime
class Time(IFormatter):
    def __init__(self):
        self.value = None
        self.long = LongDate()
        self.short = ShortDate()
        self.mid = MidDate()

        self.default = Defualt()

        self.long.set_next(self.short)
        self.short.set_next(self.mid)
        self.mid.set_next(self.default)



    def format(self,value,format_sepec):
        if 'datetime' in format_sepec:
            timestamp = float(value)
            value = self.long.run(timestamp,format_sepec)


        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor


class LongDate:

    def run(self,value,format_sepec):
        if format_sepec['datetime'] =='long':
            mask = '%Y:%m:%d %I:%M %p' if 'datetime_mode'  in format_sepec and  format_sepec['datetime_mode']==12 else '%Y:%m:%d %H:%M:%S:%f'

            formatted_datetime = datetime.datetime.fromtimestamp(value).strftime(mask)
            value = formatted_datetime

        return self.go_next.run(value,format_sepec)

    def set_next(self,go_next):
        self.go_next = go_next


class MidDate:

    def run(self,value,format_sepec):

        if format_sepec['datetime'] =='mid':

            mask = '%Y:%m:%d %H:%M:%S' if 'datetime_mode'  in format_sepec and  format_sepec['datetime_mode']==24 else  '%Y:%m:%d %I:%M %p'

            formatted_datetime = datetime.datetime.fromtimestamp(value).strftime(mask)
            value = formatted_datetime
            return self.go_next.run(value,format_sepec)
        return self.go_next.run(value,format_sepec)

    def set_next(self,go_next):
        self.go_next = go_next

class ShortDate:

    def run(self,value,format_sepec):
        if format_sepec['datetime'] =='short':

            mask = '%H:%M:%S' if 'datetime_mode'  in format_sepec and  format_sepec['datetime_mode']==24 else  '%I:%M %p'

            formatted_datetime = datetime.datetime.fromtimestamp(value).strftime(mask)
            value = formatted_datetime
        return self.go_next.run(value,format_sepec)

    def set_next(self,go_next):
        self.go_next = go_next

class Defualt:

    def run(self,value,format_sepec):


        if format_sepec['datetime']!='long' and  format_sepec['datetime']!='short' and format_sepec['datetime'] != 'mid':
            formatted_datetime = datetime.datetime.fromtimestamp(value).strftime(format_sepec['datetime'])
            value = formatted_datetime[:-int(format_sepec['time_precision'])] if 'time_precision' in format_sepec else  formatted_datetime

        return value


    def set_next(self,go_next):
        self.go_next = go_next





