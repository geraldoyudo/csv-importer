import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from db.sqlite_person_dao import SQLiteRecordPersonDAO
from db.person_entity import PersonEntity, INVALID_PERSON

sample_person = PersonEntity(
                    first="Gerald", 
                    last = "Oyudo",
                    address = "Some address st.",
                    state = "Lagos",
                    town = "Okota",
                    zipcode = "123"
                )

class TestSQLitePersonDAO(unittest.TestCase):
    def setUp(self):
        self.sqlite_dao = SQLiteRecordPersonDAO("test.db")
        self.sqlite_dao.intialize_database()
        pass

    def test_save_person_list(self):
        row_count = self.sqlite_dao.save_data_entities([sample_person])
        self.assertEqual(1, row_count)

    def test_save_person_list_with_invalid_person(self):
        row_count = self.sqlite_dao.save_data_entities([sample_person,INVALID_PERSON])
        self.assertEqual(1, row_count)

if __name__ == '__main__':
    unittest.main()