import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from providers.data_store import DataStore
from models.data_save_stats import DataSaveStats

class MockDataStore(DataStore):
    def saveDataList(self, dataList):
        self.dataList = dataList
        dataListLength = len(dataList)
        return DataSaveStats(dataListLength, dataListLength)