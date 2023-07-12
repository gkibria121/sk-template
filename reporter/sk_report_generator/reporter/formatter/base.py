from abc import ABC, abstractmethod


class IFormatter(ABC):

    @abstractmethod
    def format(self,value,condition,format_sepec):
        pass

    @abstractmethod
    def set_successor(self, successor):
        pass


class IFormatHandler(ABC):

    @abstractmethod
    def handle(self, value, condition, format_specs, format_pattern):
        pass

    @abstractmethod
    def set_successor(self, successor):
        pass
