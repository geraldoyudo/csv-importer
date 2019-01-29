import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from providers.mock_data_store import MockDataStore
from providers.specs.reference_csv_data import referenceCSVData

class TestMockDataStore(unittest.TestCase):
    def setUp(self):
        self.dataStore = MockDataStore()
        pass

    def test_save_data_list(self):
        dataListStats = self.dataStore.saveDataList(referenceCSVData)
        self.assertEqual(2, dataListStats.totalRecords)
        self.assertEqual(2, dataListStats.totalSavedRecords)

if __name__ == '__main__':
    unittest.main()