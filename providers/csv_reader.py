import abc

class CSVReader(abc.ABC):
    @abc.abstractmethod
    def read(self, sourceName):
        pass

class CSVReadException(Exception):
    pass