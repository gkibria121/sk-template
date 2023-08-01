from ..base import IFormatter
import regex as re


class DefaultCustomFormat(IFormatter):
    def __init__(self):
        self.value = None

    def format(self, value, format_sepec, format_pattern=''):
        return value

    def set_successor(self, successor):
        pass
