import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from providers.person_store import PersonStore
from models.data_save_stats import DataSaveStats
from db.sqlite_person_dao import SQLiteRecordPersonDAO
from db.person_entity import PersonEntity, INVALID_PERSON

def convert_to_person(data):
    try:
        return PersonEntity(
                    first = data["first"], 
                    last = data["last"],
                    address = data["address"],
                    state = data["state"],
                    town = data["town"],
                    zipcode = data["zipcode"]
                )
    except:
        return INVALID_PERSON

class EntityConverter:
    def convert_to_entity_list(self, data_list):
        entity_list = []
        for data in data_list:
            entity_list.append(
                convert_to_person(data)
            )
        return entity_list

class SQLitePersonStore(PersonStore):
    db = "test.db"

    def __init__(self, db):
        self.db = db
        self.person_dao = SQLiteRecordPersonDAO(self.db)
        self.entity_converter = EntityConverter()
        
    def save_person_list(self, person_list):
        person_entity_list = self.entity_converter.convert_to_entity_list(person_list)
        row_count = self.person_dao.save_data_entities(person_entity_list)
        return DataSaveStats(len(person_list), row_count)

    def initialize(self):
        self.person_dao.intialize_database()
