import unittest
import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from providers.sqlite_person_store import SQLitePersonStore
from providers.sqlite_person_store import EntityConverter
from providers.specs.reference_csv_data import referenceCSVData
from providers.specs.reference_csv_data import referenceJSONData
from db.person_entity import INVALID_PERSON

class TestSQLitePersonStore(unittest.TestCase):
    def setUp(self):
        self.data_store = SQLitePersonStore("test.db")
        pass

    def test_entity_conversion(self):
        entity_converter = EntityConverter()
        entity_list = entity_converter.convert_to_entity_list(referenceCSVData)
        self.assertEqual(json.dumps(entity_list[0].__dict__), referenceJSONData[0])
        self.assertEqual(json.dumps(entity_list[1].__dict__), referenceJSONData[1])

    def test_entity_conversion_with_one_invalid_data(self):
        entity_converter = EntityConverter()
        data_list = list((referenceCSVData[0], {}))
        entity_list = entity_converter.convert_to_entity_list(data_list)
        self.assertEqual(json.dumps(entity_list[0].__dict__), referenceJSONData[0])
        self.assertEqual(entity_list[1], INVALID_PERSON)

    def test_save_person_list(self):
        data_list_stats = self.data_store.save_person_list(referenceCSVData)
        self.assertEqual(2, data_list_stats.totalRecords)
        self.assertEqual(2, data_list_stats.totalSavedRecords)
    
    def test_save_person_list_with_invalid_data(self):
        data_list = list((referenceCSVData[0], {}))
        data_list_stats = self.data_store.save_person_list(data_list)
        self.assertEqual(2, data_list_stats.totalRecords)
        self.assertEqual(1, data_list_stats.totalSavedRecords)

if __name__ == '__main__':
    unittest.main()