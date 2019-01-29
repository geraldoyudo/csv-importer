import abc

class DataStore(abc.ABC):
    @abc.abstractmethod
    def saveDataList(self, dataList):
        pass