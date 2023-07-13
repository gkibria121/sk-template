import regex as re
import math


class MethodDefault:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):
        return value
