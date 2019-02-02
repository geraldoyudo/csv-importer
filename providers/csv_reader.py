import abc

class CSVReader(abc.ABC):
    @abc.abstractmethod
    def read(self, source_name):
        pass

class CSVReadException(Exception):
    pass