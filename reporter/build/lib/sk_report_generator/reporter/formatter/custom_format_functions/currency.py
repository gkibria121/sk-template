from ..base import IFormatter
import regex as re
class Currency(IFormatter):
    def __init__(self):
        self.value = None
        self.bdt = BDT()
        self.usd = USD()
        self.default = Default()
        self.bdt.set_next(self.usd)
        self.usd.set_next(self.default)



    def format(self,value,format_sepec):

        if 'currency' in format_sepec:
            precision = format_sepec['currency_precision'] if 'currency_precision' in format_sepec else '2'
            value = self.bdt.run(value,format_sepec['currency'],precision)

        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor

class USD:


    def run(self,value,unit,precision):
        if unit =='USD':
            int_part = re.search('\d+',value)[0]
            float_match = re.search(r'\.\d'+'{'+f"{precision}"+'}',value)
            float_part = float_match[0] if float_match else '.0'
            value = format(int(int_part),',')
            value = value+float_part
        return self.go_next.run(value,unit)
    def set_next(self,go_next):
        self.go_next = go_next

class BDT:
    def __init__(self):
        self.get_format = GetBDTFormat()

    def run(self,value,unit,precision):
        if unit =='BDT':
            int_part = re.search('\d+',value)[0]
            float_match = re.search(r'\.\d'+'{'+f"{precision}"+'}',value)
            float_part = float_match[0] if float_match else '.0'
            number_str = str(int_part)[::-1]
            formatted_number = self.get_format.run(number_str)
            value =  formatted_number[::-1]+float_part

        return self.go_next.run(value,unit,precision)

    def set_next(self,go_next):
        self.go_next = go_next



class Default:
    def run(self,value,unit):
        return value


class GetBDTFormat:


    def run(self,number_str):
        formatted_number=''
        while number_str!='':
            formatted_number = formatted_number+number_str[:3]+',' if len(number_str)>3 else formatted_number+number_str[:3]
            number_str = number_str[3:]
            formatted_number =formatted_number+number_str[:2]+',' if len(number_str)>2 else formatted_number+number_str[:2]
            number_str = number_str[2:]
            formatted_number =formatted_number+number_str[:2]+','if len(number_str)>2 else formatted_number+number_str[:2]
            number_str = number_str[2:]
        return formatted_number


