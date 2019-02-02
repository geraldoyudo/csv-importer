import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from providers.person_store import PersonStore
from models.data_save_stats import DataSaveStats
from db.sqlite_person_dao import SQLiteRecordPersonDAO
from db.person_entity import PersonEntity
    
class EntityConverter:
    def convertToEntityList(self, dataList):
        entityList = []
        for data in dataList:
            entityList.append(
                PersonEntity(
                    first = data["first"], 
                    last = data["last"],
                    address = data["address"],
                    state = data["state"],
                    town = data["town"],
                    zipcode = data["zipcode"]
                )
            )
        return entityList

class SQLitePersonStore(PersonStore):
    db = "test.db"

    def __init__(self, db):
        self.db = db
        self.recordDao = SQLiteRecordPersonDAO(self.db)
        self.entityConverter = EntityConverter()
        
    def savePersonList(self, personList):
        personEntityList = self.entityConverter.convertToEntityList(personList)
        row_count = self.recordDao.save_data_entities(personEntityList)
        return DataSaveStats(len(personList), row_count)

    def initialize(self):
        self.recordDao.intialize_database()