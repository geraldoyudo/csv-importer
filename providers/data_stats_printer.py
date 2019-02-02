import abc

class DataStatsPrinter(abc.ABC):
    @abc.abstractmethod
    def print(self, dataSaveStats):
        pass
