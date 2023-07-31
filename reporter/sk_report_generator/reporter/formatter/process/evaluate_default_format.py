import regex as re
class EvaluateDefaultFormat:
    def run(self,value,format_pattern):
        value = str(value)
        digit = re.sub(r'[,.e\+\-]','',value).isdigit()
        if digit:
            try:
                f_value = eval(value)
            except:
                f_value = f'"{value}"'

        else:
            f_value = f'"{value}"'

        value =eval(f"format({f_value},format_pattern)")


        return value
