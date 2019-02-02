import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from providers.mock_person_store import MockPersonStore
from providers.specs.reference_csv_data import referenceCSVData

class TestMockPersonStore(unittest.TestCase):
    def setUp(self):
        self.personStore = MockPersonStore()
        pass

    def test_save_person_list(self):
        dataListStats = self.personStore.savePersonList(referenceCSVData)
        self.assertEqual(2, dataListStats.totalRecords)
        self.assertEqual(2, dataListStats.totalSavedRecords)

if __name__ == '__main__':
    unittest.main()