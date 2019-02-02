import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from db.sqlite_record_data_dao import SQLiteRecordDataDAO
from db.data_entity import DataEntity

class TestSQLiteRecordDataDAO(unittest.TestCase):
    def setUp(self):
        self.sqliteDao = SQLiteRecordDataDAO("test.db")
        self.sqliteDao.intialize_database()
        pass

    def test_save_data_list(self):
        row_count = self.sqliteDao.save_data_entities(
            [
                DataEntity(
                    first="Gerald", 
                    last = "Oyudo",
                    address = "Some address st.",
                    state = "Lagos",
                    town = "Okota",
                    zipcode = "123"
                )
            ]
            )
        self.assertEqual(1, row_count)

if __name__ == '__main__':
    unittest.main()