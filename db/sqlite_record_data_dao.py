import sqlite3

class SQLiteRecordDataDAO:
    db = "test.db"

    def __init__(self, db):
        self.db = db

    def intialize_database(self):
        conn = sqlite3.connect(self.db)
        db = conn.cursor()
        # Create table
        db.execute("drop table record_data")
        db.execute('''create table if not exists record_data
                    (id integer primary key , json text not null)''')
        conn.commit()
        conn.close()
    
    def save_data_entities(self, data_entity_list):
        dataList = []
        for data in data_entity_list:
            dataList.append(tuple((data.entityJson,)))
        conn = sqlite3.connect(self.db)
        db = conn.cursor()
        db.executemany("insert into record_data(json) values (?)", dataList)
        conn.commit()
        conn.close()
        return db.rowcount