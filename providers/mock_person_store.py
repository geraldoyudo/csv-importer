import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from providers.person_store import PersonStore
from models.data_save_stats import DataSaveStats

class MockPersonStore(PersonStore):
    def save_person_list(self, person_list):
        self.person_list = person_list
        person_list_length = len(person_list)
        return DataSaveStats(person_list_length, person_list_length)
