import sys
import os
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from providers.data_store import DataStore
from models.data_save_stats import DataSaveStats
from db.sqlite_record_data_dao import SQLiteRecordDataDAO
from db.data_entity import DataEntity
    
class EntityConverter:
    def convertToEntityList(self, dataList):
        entityList = []
        for data in dataList:
            entityList.append(DataEntity(data))
        return entityList

class SQLiteDataStore(DataStore):
    db = "test.db"

    def __init__(self, db):
        self.db = db
        self.recordDao = SQLiteRecordDataDAO(self.db)
        self.entityConverter = EntityConverter()
        
    def saveDataList(self, dataList):
        entityList = self.entityConverter.convertToEntityList(dataList)
        row_count = self.recordDao.save_data_entities(entityList)
        return DataSaveStats(len(dataList), row_count)

    def initialize(self):
        self.recordDao.intialize_database()