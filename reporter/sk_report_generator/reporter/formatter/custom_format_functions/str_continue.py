from ..base import IFormatter

class StrContinue(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,condition,format_sepec):
        if 'continue' in format_sepec:
            if condition == None:
                char = int(format_sepec['continue'])
                if len(value)<=char:
                    pass
                else:
                    value = eval(f"value[:{char}]")
                    if len(value)<=3:
                        pass
                    else:

                        value = value[:-3]+'...'




        return self.successor.format(value,condition,format_sepec)

    def set_successor(self,successor):
        self.successor= successor