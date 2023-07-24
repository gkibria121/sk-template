import regex as re
class ProcessCondition:
    def run(self,condition):
        reslut =re.search(r'^\((.*)\)$',condition)
        if reslut:
            condition =reslut[1]
        return condition
