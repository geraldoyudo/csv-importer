import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from providers.file_csv_reader import FileCSVReader, INVALID_DATA
from providers.specs.reference_csv_data import reference_csv_data
from providers.csv_reader import CSVReadException

class TestFileCSVReader(unittest.TestCase):
    def initialize_with_csv_file(self, file_name):
        self.file_csv_reader = FileCSVReader()
        self.data = self.file_csv_reader.read(os.path.dirname(__file__) + file_name)

    def initialize_with_valid_csv(self):
        self.initialize_with_csv_file("/sample.csv")

    def test_given_sample_csv_file_should_read_correct_number_of_records(self):
        self.initialize_with_valid_csv()
        self.assertEqual(2, len(self.data))

    def test_given_sample_csv_file_should_read_each_record_correctly(self):
        self.initialize_with_valid_csv()
        self.assertDictEqual(reference_csv_data[0], self.data[0])
        self.assertDictEqual(reference_csv_data[1], self.data[1])
    
    def test_given_csv_with_insufficient_columns_when_read_should_throw_exception(self):
        self.assertRaises(CSVReadException, self.initialize_with_csv_file, "./insufficient-header.csv")
        pass
    
    def test_given_csv_with_invalid_columns_when_read_should_throw_exception(self):
        self.assertRaises(CSVReadException, self.initialize_with_csv_file, "./invalid-header.csv")
        pass
    
    def test_given_csv_with_invalid_rows_when_read_should_ignore_invalid_rows(self):
        self.initialize_with_csv_file("/invalid-rows.csv")
        self.assertEqual(2, len(self.data))
        self.assertDictEqual(reference_csv_data[0], self.data[0])
        self.assertDictEqual(INVALID_DATA, self.data[1])
        pass

if __name__ == '__main__':
    unittest.main()