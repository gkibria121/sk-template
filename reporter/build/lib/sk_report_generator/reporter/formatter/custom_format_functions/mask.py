from ..base import IFormatter
import regex as re
class Mask(IFormatter):
    def __init__(self):
        self.value = None
        self.mask = GetPattern()
        self.eval_mask = EvaluateMask()

    def format(self,value,format_sepec):

        if 'mask' in format_sepec:
            value = str(value)

            mask = format_sepec['mask']
            pattern,sub_pattern = self.mask.run(mask)
            value = self.eval_mask.run(value,pattern,sub_pattern)
        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor

class GetPattern:


    def run(self,mask):

        matches = re.findall(r'[#]+',mask)
        pattern = ''
        for match in matches:
            count =len(match)
            pattern += '([\d\.]{'+str(count)+'})'
        mask_pattern = re.sub(r'([#]+)', lambda match, count=iter(range(1, 100)): '\\'+str(next(count)), mask)
        return pattern,mask_pattern

class EvaluateMask:
    def run(self,value,pattern,mask_pattern):

        masked_value = re.sub(pattern, mask_pattern, value)
        return masked_value
