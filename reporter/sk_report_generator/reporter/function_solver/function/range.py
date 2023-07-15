import regex as re
import math



class Range:
    def __init__(self):
        self.default_range = DefaultRange()
        self.custom_range = CustomRange()
        self.default = Default()

        self.default_range.set_next(self.custom_range)
        self.custom_range.set_next(self.default)

    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='range':

            if condition !='':
                args = condition.split(',')
                value = self.default_range.run(value,args)

        return self.go_next.run(value,method,condition)


class DefaultRange:


    def run(self,string,args):
        if len(args) ==1:
            string = string[0:int(args[0])]

        if len(args)==2 and args[1].isdigit():
            string = string[int(args[0]):int(args[1])]

        return self.go_next.run(string,args)

    def set_next(self,go_next):
        self.go_next = go_next



class CustomRange:


    def run(self,string,args):

        if len(args) ==2 and not args[1].isdigit():
            if (args[1]=='c'):
                string = string[0:int(args[0])]
            if ((args[1]=='w')):
                string = re.search(r'^\b(\s*\w+){'+args[0]+'}',string)
                if string:
                    string = string.group(0)




        if len(args) ==3:
            if (args[2]=='c'):
                string = string[int(args[0]):int(args[1])]
            if ((args[2]=='w')):
                string = re.sub(r'^\b(\s*\w+\s*){'+args[0]+'}','',string)
                steps = int(args[1])-int(args[0])
                string = re.search(r'^\b(\s*\w+\s*){'+str(steps)+'}',string).group(0)

        return self.go_next.run(string,args)

    def set_next(self,go_next):
        self.go_next = go_next




class Default:

    def run(self,string,args):

        return string

    def set_next(self,go_next):
        self.go_next = go_next













