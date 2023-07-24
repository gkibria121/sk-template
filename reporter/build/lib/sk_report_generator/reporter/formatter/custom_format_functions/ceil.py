from ..base import IFormatter


class Ceil(IFormatter):
    def __init__(self):
        self.successor = None
        self.value = None

        self.ceil = CeilSpec()
        self.ceil_significance =  CeilSignificance()
        self.default = Default()
        self.ceil.set_next(self.ceil_significance)
        self.ceil_significance.set_next(self.default)

    def format(self, value, format_sepec):

        value = self.ceil.run(value, format_sepec)

        return self.successor.format(value, format_sepec)

    def set_successor(self, successor):
        self.successor = successor


class CeilSignificance:

    def run(self,value,format_sepec):
        if 'ceil-significance' in format_sepec:
            precision = float(format_sepec['ceil-significance'])
            value = float(value)
            mod = value % precision

            if mod == 0:
                value = str(value)
            else:
                value = str(value + precision - mod)

        return self.go_next.run(value,format_sepec)

    def set_next(self,go_next):
        self.go_next = go_next

class CeilSpec:

    def run(self,value,format_sepec):
        if 'ceil' in format_sepec:
            if format_sepec['ceil'] == True:
                value = float(value)
                mod = value%1
                if mod ==0:
                    value = str(value)
                else:
                    value = str(value+1-mod)
        return self.go_next.run(value,format_sepec)

    def set_next(self,go_next):
        self.go_next = go_next

class Default:

    def run(self,value,format_sepec):
        return value