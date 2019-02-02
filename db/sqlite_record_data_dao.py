import sqlite3

class SQLiteRecordDataDAO:
    db = "test.db"

    def __init__(self, db):
        self.db = db

    def intialize_database(self):
        conn = sqlite3.connect(self.db)
        db = conn.cursor()
        # Create table
        # first,last,address,town,state,pobox
        db.execute('''create table if not exists person
                    (
                        id integer primary key , 
                        first text not null,
                        last text not null,
                        address text not null,
                        town text not null,
                        state text not null,
                        zipcode text not null
                    )''')
        conn.commit()
        conn.close()
    
    def save_data_entities(self, data_entity_list):
        dataList = []
        for data in data_entity_list:
            dataList.append(tuple((data.first, data.last, data.address,
            data.town, data.state, data.zipcode)))
        conn = sqlite3.connect(self.db)
        db = conn.cursor()
        db.executemany("insert into person(first,last,address,town,state,zipcode) values (?,?,?,?,?,?)", dataList)
        conn.commit()
        conn.close()
        return db.rowcount