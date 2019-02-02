import unittest
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from providers.sqlite_person_store import SQLitePersonStore
from providers.sqlite_person_store import EntityConverter
from providers.specs.reference_csv_data import referenceCSVData
from providers.specs.reference_csv_data import referenceJSONData

class TestSQLitePersonStore(unittest.TestCase):
    def setUp(self):
        self.dataStore = SQLitePersonStore("test.db")
        pass

    def test_entity_conversion(self):
        entityConverter = EntityConverter()
        entityList = entityConverter.convertToEntityList(referenceCSVData)
        self.assertEqual(json.dumps(entityList[0].__dict__), referenceJSONData[0])
        self.assertEqual(json.dumps(entityList[1].__dict__), referenceJSONData[1])

    def test_save_person_list(self):
        dataListStats = self.dataStore.savePersonList(referenceCSVData)
        self.assertEqual(2, dataListStats.totalRecords)
        self.assertEqual(2, dataListStats.totalSavedRecords)

if __name__ == '__main__':
    unittest.main()