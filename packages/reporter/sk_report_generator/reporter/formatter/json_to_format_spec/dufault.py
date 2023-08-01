from ..base import IFormatter2
import regex as re


class DefaultFormat(IFormatter2):
    def __init__(self):
        self.value = None

    def handle(self,format_sepec, format_pattern):


        return format_pattern,format_sepec


    def set_successor(self, successor):
        pass
