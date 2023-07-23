from ..base import IFormatter

class Floor(IFormatter):
    def __init__(self):
        self.value = None
        self.floor = FloorSpec()
        self.floor_significance =  FloorSignificance()
        self.default = Default()
        self.floor.set_next(self.floor_significance)
        self.floor_significance.set_next(self.default)

    def format(self,value,format_sepec):

        value = self.floor.run(value,format_sepec)

        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor

class FloorSignificance:

    def run(self,value,format_sepec):
        if 'floor-significance' in format_sepec:
            precision = float(format_sepec['floor-significance'])
            value = float(value)
            mod = round(value%precision,9)

            if mod ==0 or mod==precision:
                value = str(value)
            else:
                value = str(value-mod)
        return self.go_next.run(value,format_sepec)

    def set_next(self,go_next):
        self.go_next = go_next

class FloorSpec:

    def run(self,value,format_sepec):
        if 'floor' in format_sepec:
            if format_sepec['floor'] == True:
                value = float(value)
                mod = value%1
                if mod ==0:
                    value = str(value)
                else:
                    value = str(value-mod)
        return self.go_next.run(value,format_sepec)

    def set_next(self,go_next):
        self.go_next = go_next

class Default:

    def run(self,value,format_sepec):
        return value
