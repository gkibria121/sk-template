from ..base import IFormatter
import datetime
class Time(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,condition,format_sepec):
        if 'datetime' in format_sepec:
            if condition == None:
                timestamp = float(value)
                formatted_datetime = datetime.datetime.fromtimestamp(timestamp).strftime(format_sepec['datetime'])
                value = formatted_datetime[:-int(format_sepec['time_precision'])] if 'time_precision' in format_sepec else  formatted_datetime








        return self.successor.format(value,condition,format_sepec)

    def set_successor(self,successor):
        self.successor= successor