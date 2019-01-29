import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from providers.sqlite_data_store import SQLiteDataStore
from providers.sqlite_data_store import EntityConverter
from providers.specs.reference_csv_data import referenceCSVData
from providers.specs.reference_csv_data import referenceJSONData

class TestSQLiteDataStore(unittest.TestCase):
    def setUp(self):
        self.dataStore = SQLiteDataStore("test.db")
        pass

    def test_entity_conversion(self):
        entityConverter = EntityConverter()
        entityList = entityConverter.convertToEntityList(referenceCSVData)
        self.assertEqual(entityList[0].entityJson, referenceJSONData[0])
        self.assertEqual(entityList[1].entityJson, referenceJSONData[1])

    def test_save_data_list(self):
        dataListStats = self.dataStore.saveDataList(referenceCSVData)
        self.assertEqual(2, dataListStats.totalRecords)
        self.assertEqual(2, dataListStats.totalSavedRecords)

if __name__ == '__main__':
    unittest.main()