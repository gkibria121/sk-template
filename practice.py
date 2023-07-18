import  re
class Formater:
    def __init__(self):
        self.count = 0
    def format_with_mask(self,phone_number,pattern,mask_pattern):

        masked_number = re.sub(pattern, mask_pattern, phone_number)
        return masked_number


    def mask_to_pattern(self,mask):
        matches = re.findall(r'[#]+',mask)
        pattern = ''
        for match in matches:
            count =len(match)
            pattern += '(\d{'+str(count)+'})'
        mask_pattern = re.sub(r'([#]+)', lambda match, count=iter(range(1, 100)): '\\'+str(next(count)), mask)
        return pattern,mask_pattern

# Example usage:
phone_number = "1234567890"
mask = '(###) ###-####'
formatter = Formater()
pattern,mask_pattern =formatter.mask_to_pattern(mask)
masked_number = formatter.format_with_mask(phone_number,pattern,mask_pattern)
print(masked_number)
