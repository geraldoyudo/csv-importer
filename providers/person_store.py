import abc

class PersonStore(abc.ABC):
    @abc.abstractmethod
    def savePersonList(self, personList):
        pass