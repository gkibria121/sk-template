from ..base import IFormatter

class StrContinue(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,format_sepec):
        if 'continue' in format_sepec:
            char = int(format_sepec['continue'])
            if len(value)<=char:
                pass
            else:
                value = eval(f"value[:{char}]")
                if len(value)<=3:
                    pass
                else:

                    value = value[:-3]+'...'




        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor