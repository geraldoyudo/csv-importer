import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import io
import unittest.mock

from providers.console_data_stats_printer import ConsoleDataStatsPrinter
from models.data_save_stats import DataSaveStats

class TestConsoleDataStatsPrinter(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        self.dataStatsPrinter.print(self.data)
        self.assertEqual(expected_output, mock_stdout.getvalue())

    def setUp(self):
        self.dataStatsPrinter = ConsoleDataStatsPrinter()
        self.data = DataSaveStats(5, 5)

    def test_print(self):
        self.assert_stdout("Number of records = 5\nNumber of inserted records = 5\n")

if __name__ == '__main__':
    unittest.main()