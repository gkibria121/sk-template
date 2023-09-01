from .add import Addition
from .sub import Subtraction
from .division import Division
from .multiply import Multiplication
from .function import Function
from .bracket import Bracket
from .reference_process import ReferenceProcess




class OperatorsProcess:

    def __init__(self):
        self.bracket = Bracket()
        self.function = Function()
        self.division = Division()
        self.multiplication = Multiplication()
        self.addition = Addition()
        self.subtraction = Subtraction()
        self.reference_process = ReferenceProcess()


        self.bracket.set_next(self.function)
        self.function.set_next(self.subtraction)
        self.subtraction.set_next(self.addition)
        self.addition.set_next(self.multiplication)
        self.multiplication.set_next(self.division)

        self.division.set_next(self.reference_process)

        self.reference_process.set_next(type('Default',(),{'process' : lambda match: match}))



    def run(self,expression):

        return self.bracket.process(expression)


    def set_argument_process(self,process):
        self.argument_process = process
        self.reference_process.set_argument_process(self.argument_process)