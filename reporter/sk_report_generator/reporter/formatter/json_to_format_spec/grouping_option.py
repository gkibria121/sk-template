import regex as re


class GroupingOptionHandler:

    def __init__(self):
        self.successor = None

    def handle(self, value, format_specs, format_pattern):
        if 'grouping_option' in format_specs:
            format_pattern = re.sub(r'\{grouping_option\}', str(format_specs['grouping_option']), format_pattern)
            del format_specs['grouping_option']
        format_pattern = re.sub(r'\{grouping_option\}', '', format_pattern)

        return self.successor.handle(value, format_specs, format_pattern)

    def set_successor(self, successor):
        self.successor = successor
