import abc

class DataStatsPrinter(abc.ABC):
    @abc.abstractmethod
    def print(self, data_save_stats):
        pass
