import regex as re
import math


class Index:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):

        if method in ['first_index_of','index_of','index']:
            if condition=='':
                pass
            if condition!='':
                try:
                    value =eval(f"value.index({condition})")
                except ValueError:
                    value = -1
        if method == 'last_index_of':
            if condition=='':
                pass
            if condition!='':
                try:
                    index =eval(f"value[::-1].index({condition})")
                    value = len(value)-index-1
                except ValueError:
                    value = -1


        return self.go_next.run(value,method,condition)