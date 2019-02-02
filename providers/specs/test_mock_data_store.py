import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from providers.mock_person_store import MockPersonStore
from providers.specs.reference_csv_data import referenceCSVData

class TestMockPersonStore(unittest.TestCase):
    def setUp(self):
        self.person_store = MockPersonStore()
        pass

    def test_save_person_list(self):
        data_list_stats = self.person_store.save_person_list(referenceCSVData)
        self.assertEqual(2, data_list_stats.totalRecords)
        self.assertEqual(2, data_list_stats.totalSavedRecords)

if __name__ == '__main__':
    unittest.main()