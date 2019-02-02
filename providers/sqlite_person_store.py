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
    def convert_to_entity_list(self, dataList):
        entityList = []
        for data in dataList:
            entityList.append(
                convert_to_person(data)
            )
        return entityList

class SQLitePersonStore(PersonStore):
    db = "test.db"

    def __init__(self, db):
        self.db = db
        self.recordDao = SQLiteRecordPersonDAO(self.db)
        self.entityConverter = EntityConverter()
        
    def save_person_list(self, personList):
        personEntityList = self.entityConverter.convert_to_entity_list(personList)
        row_count = self.recordDao.save_data_entities(personEntityList)
        return DataSaveStats(len(personList), row_count)

    def initialize(self):
        self.recordDao.intialize_database()