import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from providers.file_csv_reader import FileCSVReader
from providers.specs.reference_csv_data import referenceCSVData

class TestFileCSVReader(unittest.TestCase):
    def setUp(self):
        self.fileCsvReader = FileCSVReader()
        self.data = self.fileCsvReader.read(os.path.dirname(__file__) + "/sample.csv")

    def test_given_sample_csv_file_should_read_correct_number_of_records(self):
        self.assertEqual(2, len(self.data))

    def test_given_sample_csv_file_should_read_each_record_correctly(self):
        self.assertDictEqual(referenceCSVData[0], self.data[0])
        self.assertDictEqual(referenceCSVData[1], self.data[1])

if __name__ == '__main__':
    unittest.main()