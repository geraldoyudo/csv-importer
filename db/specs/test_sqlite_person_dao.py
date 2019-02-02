import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from db.sqlite_person_dao import SQLiteRecordPersonDAO
from db.person_entity import PersonEntity

class TestSQLitePersonDAO(unittest.TestCase):
    def setUp(self):
        self.sqliteDao = SQLiteRecordPersonDAO("test.db")
        self.sqliteDao.intialize_database()
        pass

    def test_save_person_list(self):
        row_count = self.sqliteDao.save_data_entities(
            [
                PersonEntity(
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