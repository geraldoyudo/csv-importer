import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from providers.person_store import PersonStore
from models.data_save_stats import DataSaveStats

class MockPersonStore(PersonStore):
    def save_person_list(self, personList):
        self.personList = personList
        personListLength = len(personList)
        return DataSaveStats(personListLength, personListLength)