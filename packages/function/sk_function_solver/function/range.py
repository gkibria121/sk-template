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


    def run(self,array,args):
        if len(args) ==1:
            array = array[int(args[0]):]

        if len(args)==2 and re.sub(r'[-+]','',args[1]).isdigit():
            array = array[int(args[0]):int(args[1])]
        if len(args)==3 and re.sub(r'[-+]','',args[1]).isdigit() and re.sub(r'[-+]','',args[2]).isdigit():
            array = array[int(args[0]):int(args[1]):int(args[2])]

        return self.go_next.run(array,args)

    def set_next(self,go_next):
        self.go_next = go_next



class CustomRange:


    def run(self,string,args):

        if len(args) ==2 and not re.sub(r'[-+]','',args[1]).isdigit():
            if (args[1]=='c'):
                string = string[int(args[0]):]
            if ((args[1]=='w')):
                wordlist = re.split(r'\s+',string)
                string =' '.join(wordlist[int(args[0]):])

        if len(args) ==3:
            if (args[2]=='c'):
                string = string[int(args[0]):int(args[1])]
            if ((args[2]=='w')):
                wordlist = re.split(r'\s+',string)
                string = ' '.join(wordlist[int(args[0]):int(args[1])])

        if len(args) ==4:
            if (args[3]=='c'):
                string = string[int(args[0]):int(args[1]):int(args[2])]
            if ((args[3]=='w')):
                wordlist = re.split(r'\s+',string)
                string =' '.join( wordlist[int(args[0]):int(args[1]):int(args[2])])
        return self.go_next.run(string,args)

    def set_next(self,go_next):
        self.go_next = go_next




class Default:

    def run(self,string,args):

        return string

    def set_next(self,go_next):
        self.go_next = go_next













