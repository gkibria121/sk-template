import regex as re


class PadHandler:

    def __init__(self):
        self.successor = None

    def handle(self, format_specs, format_pattern):
        if 'pad' in format_specs:
            format_pattern = re.sub(r'\{pad\}', str(format_specs['pad']), format_pattern)
            del format_specs['pad']

        format_pattern = re.sub(r'\{pad\}', '', format_pattern)

        return self.successor.handle( format_specs, format_pattern)

    def set_successor(self, successor):
        self.successor = successor
