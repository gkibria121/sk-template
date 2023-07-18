from .custom_format_functions.floor import Floor
from .custom_format_functions.mask import Mask
from .custom_format_functions.currency import Currency
from .custom_format_functions.datetime import Time
from .custom_format_functions.round import Round
from .custom_format_functions.ceil import Ceil
from .custom_format_functions.str_continue import StrContinue
from .json_to_format_spec.width import WidthHandler
from .json_to_format_spec.align import AlignHandler
from .json_to_format_spec.fill import FillHandler
from .json_to_format_spec.grouping_option import GroupingOptionHandler
from .json_to_format_spec.pad import PadHandler
from .json_to_format_spec.precision import PrecisionHandler
from .json_to_format_spec.sign import SignHandler
from .json_to_format_spec.type import TypeHandler
from .process.custom_format_process import CustomFormatProcess
from .default import Default


class CustomFormat:

    def __init__(self):
        self.custom_format_process =CustomFormatProcess()


        self.floor = Floor()
        self.time = Time()
        self.currency = Currency()
        self.ceil = Ceil()
        self.str_continue = StrContinue()
        self.default = Default()
        self.width_handler = WidthHandler()
        self.align = AlignHandler()
        self.fill = FillHandler()
        self.grouping_option = GroupingOptionHandler()
        self.pad = PadHandler()
        self.precision = PrecisionHandler()
        self.sign = SignHandler()
        self.round = Round()
        self.type = TypeHandler()
        self.mask = Mask()


        self.floor.set_successor(self.time)
        self.time.set_successor(self.currency)
        self.currency.set_successor(self.round)
        self.round.set_successor(self.str_continue)
        self.str_continue.set_successor(self.mask)
        self.mask.set_successor(self.ceil)
        self.ceil.set_successor(self.default)



        self.width_handler.set_successor(self.align)
        self.align.set_successor(self.fill)
        self.fill.set_successor(self.grouping_option)
        self.grouping_option.set_successor(self.pad)
        self.pad.set_successor(self.sign)
        self.sign.set_successor(self.type)
        self.type.set_successor(self.precision)
        self.precision.set_successor(self.default)

    def set_process(self,process):
        self.process = process

    def run(self,value,format_spec,format_class_list):

        if len(format_class_list)!=0:
            condition, format_specs = self.custom_format_process.run(value,format_spec, format_class_list)
            if condition:
                format_pattern = '{{value}:{fill}{align}{sign}{pad}{width}{grouping_option}{precision}{base}}'
                default_format_value, format_specs = self.width_handler.handle(value, format_specs,format_pattern)
                value = self.floor.format(default_format_value, format_specs)



        return self.go_next.run(value,format_spec,format_class_list)

    def set_next(self,go_next):

        self.go_next = go_next